"""Crawl the generated site without JavaScript and check search-critical contracts."""
import json
from datetime import datetime
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
from build_site_support import Document, ROOT, ORIGIN


def file_for(url):
    path = unquote(urlsplit(url).path).lstrip("/")
    return ROOT / (path + "index.html" if not path or path.endswith("/") else path)


def check():
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "v": "http://www.google.com/schemas/sitemap-video/1.1"}
    entries = ET.parse(ROOT / "sitemap.xml").findall("s:url", ns)
    urls = [e.findtext("s:loc", namespaces=ns) for e in entries]
    assert len(urls) == len(set(urls)) == 26
    docs = {url: Document(file_for(url).read_text(encoding="utf-8")) for url in urls}
    titles, graph = set(), {}
    for url, doc in docs.items():
        canonical = doc.one("link", rel="canonical").attrs["href"]
        assert canonical == url, (url, canonical)
        assert len(doc.elements("h1")) == 1, url
        title = doc.one("title").html()
        assert title not in titles, title
        titles.add(title)
        assert len(doc.one("meta", name="description").attrs["content"]) > 30
        assert "noindex" not in doc.one("meta", name="robots").attrs["content"]
        lang = doc.one("html").attrs["lang"]
        assert lang == ("en" if urlsplit(url).path.startswith("/en/") else "zh-Hant")
        alternates = {e.attrs["hreflang"]: e.attrs["href"] for e in doc.elements("link", rel="alternate")}
        assert set(alternates) == {"en", "zh-Hant", "x-default"}
        assert alternates[lang] == url
        for dest in alternates.values():
            other = docs[dest]
            assert any(e.attrs.get("href") == url for e in other.elements("link", rel="alternate"))
        graph[url] = set()
        for el in doc.elements():
            for attr in ("href", "src"):
                value = el.attrs.get(attr, "")
                if not value or value.startswith(("https:", "http:", "data:", "mailto:", "tel:")):
                    continue
                target = urlsplit(value)
                local = file_for(value) if target.path else file_for(url)
                assert local.is_file(), (url, value)
                if target.fragment and local.suffix == ".html":
                    target_doc = Document(local.read_text(encoding="utf-8"))
                    assert target_doc.elements(id=unquote(target.fragment)), (url, value)
                if el.tag == "a" and target.path.endswith("/"):
                    graph[url].add(ORIGIN + target.path)
        for image in doc.elements("img"):
            assert image.attrs.get("alt") and image.attrs.get("width") and image.attrs.get("height"), url
        schema = json.loads("".join(doc.one("script", type="application/ld+json").children))["@graph"]
        assert all(s["@type"] != "ProfessionalService" for s in schema)
        videos = [s for s in schema if s["@type"] == "VideoObject"]
        if "/films/" in url:
            assert len(videos) == 1 and len(doc.elements("iframe")) == 1
            video = videos[0]
            for key in ["name", "description", "thumbnailUrl", "uploadDate", "duration", "embedUrl"]:
                assert video[key]
            assert datetime.fromisoformat(video["uploadDate"]).tzinfo
            iframe = doc.one("iframe")
            assert iframe.attrs["src"].startswith(video["embedUrl"] + "?")
            assert "autoplay=1" not in iframe.attrs["src"]
            assert "srcdoc" not in iframe.attrs
            assert file_for(video["thumbnailUrl"][0]).is_file()
    reached, pending = set(), [ORIGIN + "/"]
    while pending:
        url = pending.pop()
        if url in reached:
            continue
        reached.add(url)
        pending.extend(graph.get(url, set()) - reached)
    assert set(urls) <= reached, set(urls) - reached
    english = docs[ORIGIN + "/en/"].root.html()
    assert "Every move" in english and "舞蹈教室成果發表" not in english
    assert "index,follow" not in (ROOT / "404.html").read_text(encoding="utf-8")
    assert (ROOT / ".nojekyll").exists()
    assert len(ET.parse(ROOT / "sitemap.xml").findall("s:url/v:video", ns)) == 24
    print("PASS: 26 crawlable pages; unique metadata; bilingual static content; reciprocal hreflang; local links/anchors/assets; reachable film pages; valid JSON-LD, dates and video sitemap; reserved player dimensions.")


if __name__ == "__main__":
    check()
