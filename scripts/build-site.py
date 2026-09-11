"""Build crawlable bilingual HTML using Python/Node standard libraries only."""
from __future__ import annotations

from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://yt.jamesboson.com"
UPDATED = "2026-09-12"
VOID = set("area base br col embed hr img input link meta param source track wbr".split())
TITLES = ["側影之心｜台灣舞蹈錄影・舞展成發・賽事記錄", "Taiwan Dance Videographer | JBS Street Recordings"]
DESCRIPTIONS = [
    "側影之心 JBS Street Recordings，專注台灣舞蹈錄影、舞蹈教室成果發表、高中職聯合成發、街舞賽事記錄與 KPOP 快閃。瀏覽真實拍攝作品，透過 Instagram 洽詢檔期與合作。",
    "Dance videography in Taiwan by JBS Street Recordings. Explore studio recitals, joint school showcases, dance competitions and KPOP IN PUBLIC films. Enquire on Instagram.",
]
CATEGORIES = {
    "stage": ["舞展/成發", "Showcases & Recitals"],
    "competition": ["賽事記錄", "Competitions"],
    "kpop": ["KPOP 快閃", "KPOP IN PUBLIC"],
}


class Element:
    def __init__(self, tag="", attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Element):
                yield from child.walk()

    def html(self):
        body = "".join(c.html() if isinstance(c, Element) else c for c in self.children)
        if not self.tag:
            return body
        attrs = "".join(f' {k}' if v is None else f' {k}="{escape(v, quote=True)}"' for k, v in self.attrs.items())
        return f"<{self.tag}{attrs}>" + ("" if self.tag in VOID else body + f"</{self.tag}>")

    def inner(self, value):
        self.children = [value]


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=False)
        self.root = Element()
        self.stack = [self.root]
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        el = Element(tag, attrs)
        self.stack[-1].children.append(el)
        if tag not in VOID:
            self.stack.append(el)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)

    def handle_entityref(self, name):
        self.handle_data(f"&{name};")

    def handle_charref(self, name):
        self.handle_data(f"&#{name};")

    def handle_decl(self, decl):
        self.handle_data(f"<!{decl}>")

    def handle_comment(self, data):
        self.handle_data(f"<!--{data}-->")

    def elements(self, tag=None, **attrs):
        return [e for e in self.root.walk() if (tag is None or e.tag == tag) and all(e.attrs.get(k) == v for k, v in attrs.items())]

    def one(self, tag=None, **attrs):
        matches = self.elements(tag, **attrs)
        if len(matches) != 1:
            raise ValueError(f"Expected one {tag} {attrs}, found {len(matches)}")
        return matches[0]


def asset(path):
    digest = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()[:10]
    return f"/{path}?v={digest}"


def write(path, text):
    output = ROOT / path
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(line.rstrip() for line in text.splitlines()) + "\n", encoding="utf-8", newline="\n")


def jsonld(graph):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2).replace("</", "<\\/") + "</script>"


def person():
    return {"@type": "Person", "@id": ORIGIN + "/#filmmaker", "name": "側影之心", "alternateName": "JBS Street Recordings", "url": ORIGIN + "/", "jobTitle": "Dance videographer", "homeLocation": {"@type": "Country", "name": "Taiwan"}, "sameAs": ["https://www.youtube.com/@jbs-street-recordings", "https://www.instagram.com/jbs.street.recordings/"]}


def route(lang, video=None):
    return ("/en/" if lang else "/") + (f"films/{video}/" if video else "")


def alternates(video=None):
    return "\n".join(f'<link rel="alternate" hreflang="{code}" href="{ORIGIN}{route(i, video)}">' for code, i in [("zh-Hant", 0), ("en", 1), ("x-default", 0)])


def homepage(template, films, english, lang):
    doc = Document(template)
    url = ORIGIN + route(lang)
    doc.one("html").attrs["lang"] = "en" if lang else "zh-Hant"
    if lang:
        for el in list(doc.elements()):
            key = el.attrs.get("data-i18n")
            if key in english:
                el.inner(english[key])
        for img in doc.elements("img"):
            if "data-alt-en" in img.attrs:
                img.attrs["alt"] = img.attrs["data-alt-en"]
        labels = {"主要導覽": "Main navigation", "行動版導覽": "Mobile navigation", "作品分類": "Filter films", "側影之心 JBS Street Recordings 首頁": "JBS Street Recordings home", "開啟選單": "Open menu", "關閉影片": "Close film", "合作需求範本": "Project brief template"}
        for el in doc.elements():
            label = el.attrs.get("aria-label")
            if label in labels:
                el.attrs["aria-label"] = labels[label]
            if "service-arrow" in el.attrs.get("class", ""):
                el.attrs["aria-label"] = "Enquire about filming"
    doc.one("title").inner(escape(TITLES[lang]))
    for tag, attrs in [("meta", {"name": "description"}), ("meta", {"property": "og:description"})]:
        doc.one(tag, **attrs).attrs["content"] = DESCRIPTIONS[lang]
    doc.one("meta", property="og:title").attrs["content"] = TITLES[lang]
    doc.one("meta", property="og:locale").attrs["content"] = "en_US" if lang else "zh_TW"
    doc.one("meta", property="og:url").attrs["content"] = url
    doc.one("link", rel="canonical").attrs["href"] = url
    for el in doc.elements():
        for attr in ("href", "src"):
            val = el.attrs.get(attr, "")
            if val.startswith("assets/"):
                el.attrs[attr] = "/" + val
        if el.tag == "link" and el.attrs.get("rel") == "stylesheet":
            el.attrs["href"] = asset("styles.css")
        if el.tag == "script" and el.attrs.get("src", "").startswith("app.js"):
            el.attrs["src"] = asset("app.js")
        if el.tag == "script" and el.attrs.get("src") == "/analytics.js":
            el.attrs["src"] = asset("analytics.js")
        video = el.attrs.get("data-video")
        if video:
            el.attrs["href"] = route(lang, video)
            el.attrs.pop("target", None)
            el.attrs.pop("rel", None)
            el.attrs["aria-label"] = ("Play " if lang else "播放 ") + films[video]["title"][lang]
    toggle = doc.one("a", **{"class": "language-toggle"})
    toggle.attrs.update({"href": route(1 - lang), "hreflang": "zh-Hant" if lang else "en", "aria-label": "切換繁體中文" if lang else "Switch to English"})
    toggle.inner("中" if lang else "EN")
    doc.one("a", **{"class": "text-link film-page-link"}).attrs["href"] = route(lang, "mlC6SqKO5Xs")
    head = doc.one("head")
    head.children = [c for c in head.children if not (isinstance(c, Element) and c.attrs.get("type") == "application/ld+json")]
    head.children += ["\n" + alternates(), '\n<meta name="robots" content="index,follow,max-image-preview:large,max-video-preview:-1">', '\n<meta property="og:image:alt" content="BOOMBAYAH · 2025 DANCE ON LIFE · JBS Street Recordings">']
    website = {"@type": "WebSite", "@id": ORIGIN + "/#website", "url": ORIGIN + "/", "name": "側影之心 · JBS Street Recordings", "alternateName": ["側影之心", "JBS Street Recordings"], "publisher": {"@id": ORIGIN + "/#filmmaker"}, "inLanguage": ["zh-Hant", "en"]}
    collection = {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": TITLES[lang], "description": DESCRIPTIONS[lang], "inLanguage": "en" if lang else "zh-Hant", "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@id": ORIGIN + "/#filmmaker"}, "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i, "name": f["title"][lang], "url": ORIGIN + route(lang, vid)} for i, (vid, f) in enumerate(films.items(), 1)]}}
    head.children.append("\n" + jsonld([person(), website, collection]) + "\n")
    return doc.root.html()


def film_page(video, film, meta, films, lang):
    title, credit = film["title"][lang], film["credit"][lang]
    category = CATEGORIES[film["category"]][lang]
    url = ORIGIN + route(lang, video)
    home = route(lang)
    image = f"{ORIGIN}/assets/images/{video}.webp"
    embed = f"https://www.youtube-nocookie.com/embed/{video}"
    seconds = meta["durationSeconds"]
    duration = f"{seconds // 60:02}:{seconds % 60:02}"
    page_title = f"{title}｜{category}｜側影之心" if not lang else f"{title} | {category} | JBS Street Recordings"
    description = credit.replace("｜200 萬觀看 UP", "").replace(" · 2M+ views", "")
    upload = meta["uploadDate"]
    date = upload[:10]
    labels = [
        {"home": "作品集", "details": "關於這支作品", "published": "YouTube 發布日期", "length": "影片長度", "recorded": "影像紀錄", "original": "原始影片標題", "youtube": "在 YouTube 觀看", "related": "同類作品", "contact": "洽詢類似演出的拍攝", "note": "演出、音樂與活動資訊以原始影片為準。拍攝內容、機位與交付方式依每次合作討論。", "skip": "跳至影片", "lang": "Switch to English", "milestone": "200 萬觀看 UP · YouTube 公開數據截至 2026.09.09"},
        {"home": "Portfolio", "details": "About this film", "published": "Published on YouTube", "length": "Duration", "recorded": "Filmed by", "original": "Original video title", "youtube": "Watch on YouTube", "related": "More in this category", "contact": "Discuss a similar filming project", "note": "See the original video for performance, music and event credits. Coverage, camera positions and delivery are agreed for each project.", "skip": "Skip to the film", "lang": "切換繁體中文", "milestone": "2M+ views · Public YouTube figures as of September 9, 2026"},
    ][lang]
    video_schema = {"@type": "VideoObject", "@id": url + "#video", "name": title, "description": description, "thumbnailUrl": [image], "uploadDate": upload, "duration": f"PT{seconds}S", "embedUrl": embed, "url": url, "creator": {"@id": ORIGIN + "/#filmmaker"}, "publisher": {"@id": ORIGIN + "/#filmmaker"}}
    breadcrumbs = {"@type": "BreadcrumbList", "@id": url + "#breadcrumbs", "itemListElement": [{"@type": "ListItem", "position": 1, "name": labels["home"], "item": ORIGIN + home}, {"@type": "ListItem", "position": 2, "name": title, "item": url}]}
    webpage = {"@type": "WebPage", "@id": url + "#page", "url": url, "name": page_title, "description": description, "inLanguage": "en" if lang else "zh-Hant", "mainEntity": {"@id": url + "#video"}, "breadcrumb": {"@id": url + "#breadcrumbs"}}
    related = [f'<a class="related-film" href="{route(lang, vid)}"><img src="/assets/images/{vid}.webp" width="1280" height="720" loading="lazy" decoding="async" alt="{escape(f["title"][lang], quote=True)}"><span>{escape(f["title"][lang])} ↗</span></a>' for vid, f in films.items() if f["category"] == film["category"] and vid != video][:3]
    milestone = f'<p class="views-badge">{labels["milestone"]}</p>' if video == "mlC6SqKO5Xs" else ""
    return f'''<!doctype html>
<html lang="{'en' if lang else 'zh-Hant'}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#141615">
<title>{escape(page_title)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-video-preview:-1">
<link rel="canonical" href="{url}">
{alternates(video)}
<meta property="og:type" content="video.other"><meta property="og:site_name" content="側影之心 · JBS Street Recordings">
<meta property="og:locale" content="{'en_US' if lang else 'zh_TW'}">
<meta property="og:title" content="{escape(page_title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{image}">
<meta property="og:image:width" content="1280"><meta property="og:image:height" content="720"><meta property="og:image:alt" content="{escape(title, quote=True)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="stylesheet" href="{asset('styles.css')}"><link rel="stylesheet" href="{asset('film.css')}">
<script src="{asset('analytics.js')}" defer></script>
{jsonld([person(), webpage, video_schema, breadcrumbs])}
</head>
<body class="watch-page">
<a class="skip-link" href="#film">{labels['skip']}</a>
<header class="site-header">
<a class="brand" href="{home}"><span><strong>側影之心<span class="accent">.</span></strong><small>JBS STREET RECORDINGS</small></span></a>
<nav class="watch-nav" aria-label="{'Navigation' if lang else '主要導覽'}"><a href="{home}#work">{labels['home']} ↗</a><a class="language-toggle" href="{route(1-lang, video)}" hreflang="{'zh-Hant' if lang else 'en'}" aria-label="{labels['lang']}">{'中' if lang else 'EN'}</a></nav>
</header>
<main class="watch-main wrap">
<nav class="breadcrumb" aria-label="{'Breadcrumb' if lang else '麵包屑導覽'}"><a href="{home}">{labels['home']}</a><span aria-hidden="true"> / </span><span>{escape(title)}</span></nav>
<div class="watch-heading"><p class="eyebrow section-index">{escape(category)} / JBS FILM ROOM</p><h1>{escape(title)}</h1></div>
<div class="watch-player" id="film"><iframe src="{embed}?rel=0&amp;playsinline=1&amp;enablejsapi=1" title="{escape(title, quote=True)}" width="1280" height="720" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<div class="watch-actions">{milestone}<a class="text-link" href="https://www.youtube.com/watch?v={video}" target="_blank" rel="noopener noreferrer">{labels['youtube']} ↗</a></div>
<section class="watch-details" aria-labelledby="details-title"><div><h2 id="details-title">{labels['details']}</h2><p>{escape(credit)}</p><p class="watch-note">{labels['note']}</p><details><summary>{labels['original']}</summary><p>{escape(film['sourceTitle'])}</p></details></div>
<dl><div><dt>{labels['recorded']}</dt><dd><a href="{home}#about">側影之心 · JBS Street Recordings</a></dd></div><div><dt>{labels['published']}</dt><dd><time datetime="{upload}">{date}</time></dd></div><div><dt>{labels['length']}</dt><dd>{duration}</dd></div></dl></section>
<section class="watch-related" aria-labelledby="related-title"><h2 id="related-title">{labels['related']}</h2><div class="related-grid">{''.join(related)}</div></section>
<section class="watch-contact" id="contact"><a class="button button-light" href="https://www.instagram.com/jbs.street.recordings/" target="_blank" rel="noopener noreferrer">{labels['contact']} ↗</a></section>
</main>
<footer class="site-footer wrap"><a href="{home}">側影之心 · JBS Street Recordings</a><p>© 2026 JBS Street Recordings.</p><a href="{home}#work">{labels['home']} ↑</a></footer>
</body></html>
'''


def sitemap(films, metadata):
    ns, video_ns, xhtml = "http://www.sitemaps.org/schemas/sitemap/0.9", "http://www.google.com/schemas/sitemap-video/1.1", "http://www.w3.org/1999/xhtml"
    ET.register_namespace("", ns)
    ET.register_namespace("video", video_ns)
    ET.register_namespace("xhtml", xhtml)
    root = ET.Element(f"{{{ns}}}urlset")
    for video in [None, *films]:
        for lang in [0, 1]:
            url = ET.SubElement(root, f"{{{ns}}}url")
            ET.SubElement(url, f"{{{ns}}}loc").text = ORIGIN + route(lang, video)
            ET.SubElement(url, f"{{{ns}}}lastmod").text = UPDATED
            for code, i in [("zh-Hant", 0), ("en", 1), ("x-default", 0)]:
                ET.SubElement(url, f"{{{xhtml}}}link", {"rel": "alternate", "hreflang": code, "href": ORIGIN + route(i, video)})
            if video:
                item = ET.SubElement(url, f"{{{video_ns}}}video")
                for key, value in {"thumbnail_loc": f"{ORIGIN}/assets/images/{video}.webp", "title": films[video]["title"][lang], "description": films[video]["credit"][lang], "player_loc": f"https://www.youtube-nocookie.com/embed/{video}", "duration": str(metadata[video]["durationSeconds"]), "publication_date": metadata[video]["uploadDate"]}.items():
                    ET.SubElement(item, f"{{{video_ns}}}{key}").text = value
    ET.indent(root, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n"


def main():
    # Read only the explicit content declarations, never run browser code.
    extract = "const fs=require('fs'),vm=require('vm');const s=fs.readFileSync('app.js','utf8');process.stdout.write(vm.runInNewContext(s.slice(s.indexOf('const films ='),s.indexOf('const translatedElements ='))+'JSON.stringify({films,english})'));"
    content = json.loads(subprocess.check_output(["node", "-e", extract], cwd=ROOT).decode("utf-8"))
    films, english = content["films"], content["english"]
    metadata = json.loads((ROOT / "content/video-metadata.json").read_text(encoding="utf-8"))
    template = (ROOT / "templates/home.html").read_text(encoding="utf-8")
    for lang in [0, 1]:
        write(route(lang).lstrip("/") + "index.html", homepage(template, films, english, lang))
        for video, film in films.items():
            write(route(lang, video).lstrip("/") + "index.html", film_page(video, film, metadata[video], films, lang))
    write("sitemap.xml", sitemap(films, metadata))
    print(f"Built 2 homepages and {2 * len(films)} film pages, with reciprocal language links and a video sitemap.")


if __name__ == "__main__":
    main()
