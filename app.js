"use strict";

// Every film belongs to the public JBS Street Recordings channel.
const films = {
  tiMi9QrME_Y: {
    title: ["ICONIC BY MISTAKE", "ICONIC BY MISTAKE"],
    credit: [
      "舞客星夏日派對舞蹈快閃・台中｜音樂：LE SSERAFIM × ILLIT × KATSEYE｜影像紀錄：側影之心",
      "Star Dance summer pop-up, Taichung · Music: LE SSERAFIM × ILLIT × KATSEYE · Filmed by JBS Street Recordings",
    ],
  },
  HjaXSWdrFks: {
    title: ["新生熱舞 · Rïtmo", "Rïtmo · Hsin Sheng Dance"],
    credit: [
      "演出：新生熱舞｜桃竹苗高中職聯合舞展第二十三屆 Rïtmo｜影像紀錄：側影之心",
      "Performance: Hsin Sheng Dance · 23rd Rïtmo joint school showcase · Filmed by JBS Street Recordings",
    ],
  },
  mlC6SqKO5Xs: {
    title: ["BOOMBAYAH · 佳人們誰懂", "BOOMBAYAH · Dance on Life"],
    credit: [
      "演出：佳人們誰懂｜音樂：BLACKPINK〈BOOMBAYAH〉｜2025 DANCE ON LIFE 新竹縣全國街舞大賽｜影像紀錄：側影之心",
      "Performance: 佳人們誰懂 · Music: BLACKPINK, BOOMBAYAH · 2025 Dance on Life, Hsinchu · Filmed by JBS Street Recordings",
    ],
  },
  lxSwGO8jnu0: {
    title: ["Strategy · Side Cam", "Strategy · Side Cam"],
    credit: [
      "演出：艾莉兒、曉帆、晶晶、麻由、品瑄、翊喬、真真、語晴、子涵｜音樂：TWICE〈Strategy〉｜信義區，2024.12.29｜側拍：側影之心",
      "Performance: 艾莉兒、曉帆、晶晶、麻由、品瑄、翊喬、真真、語晴、子涵 · Music: TWICE, Strategy · Xinyi, 2024.12.29 · Side camera: JBS Street Recordings",
    ],
  },
  LTzvOOpUqac: {
    title: ["GNARLY · Fireworks", "GNARLY · Fireworks"],
    credit: [
      "演出：Fireworks｜音樂：KATSEYE〈GNARLY〉｜舞客星台中夏日快閃｜影像紀錄：側影之心",
      "Performance: Fireworks · Music: KATSEYE, GNARLY · Star Dance summer pop-up, Taichung · Filmed by JBS Street Recordings",
    ],
  },
  XfOgJukNFSA: {
    title: ["三十高校街舞祭 · JAZZ", "Dance30 · JAZZ"],
    credit: [
      "演出：鶯歌、明德、松商、秀峰｜2024 SYM Dance30 三十高校街舞祭｜影像紀錄：側影之心",
      "Performance: Yingge, Mingde, Songshan & Xiufeng · 2024 SYM Dance30 · Filmed by JBS Street Recordings",
    ],
  },
};

// Trusted, authored copy only. No user input is inserted as HTML.
const english = {
  skip: "Skip to content",
  navWork: "Selected work",
  navServices: "Services",
  navAbout: "About",
  navContact: "Let’s talk",
  heroKicker: "DANCE · LIVE PERFORMANCE · FILM",
  heroLine1: "Every move.",
  heroLine2: "Worth seeing.",
  heroDesc:
    "From the street to the stage, capturing the moments you give your all.<br>Let the feeling live on, long after the last beat.",
  explore: "Explore the films",
  heroFilm: "Dance30 · JAZZ",
  intro: "You bring the energy.<span>I keep it in the frame.</span>",
  workTitle: 'Moments made for replay<span class="accent">.</span>',
  allYoutube: "More films on YouTube",
  filterAll: "All films",
  filterStreet: "K-pop / Street",
  filterStage: "Stage / Live",
  filterCompetition: "Competition",
  work1Desc: "Star Dance summer pop-up · Taichung",
  work2Title: "Rïtmo · Hsin Sheng Dance",
  work2Desc: "23rd joint school dance showcase",
  work3Desc: "佳人們誰懂 · Dance on Life, Hsinchu",
  work4Desc: "TWICE dance cover · Side cam in Xinyi",
  work5Desc: "Fireworks · Summer pop-up in Taichung",
  work6Title: "Dance30 · JAZZ",
  work6Desc: "Yingge × Mingde × Songshan × Xiufeng · SYM Dance30",
  servicesTitle: 'Your stage. My perspective<span class="accent">.</span>',
  servicesDesc:
    "For dancers, crews and event organizers.<br>Films to share, keep and come back to.",
  service1Title: "Live shows & competitions",
  service1Desc:
    "From school showcases to dance competitions, capturing formations, rhythm and the atmosphere in the room. A lasting record of the performance you worked so hard to bring to life.",
  service1Tag1: "School showcases",
  service1Tag2: "Recitals",
  service1Tag3: "Dance competitions",
  service2Title: "K-pop & street performance",
  service2Desc:
    "Documenting the details of dance covers and pop-up performances: the expressions, the connection between dancers, and the life of the street around them.",
  service2Tag2: "Street pop-ups",
  service2Tag3: "Dance crews",
  service3Title: "Side cam & dancer films",
  service3Desc:
    "Another perspective on your performance. Let’s discuss the dancer, moments and framing you want to focus on, and create footage for your own portfolio.",
  service3Tag2: "Dancer features",
  service3Tag3: "Portfolio footage",
  serviceNote:
    "Coverage, camera positions, delivery format and usage are agreed for each project. Vertical edits and highlight clips can also be discussed.",
  aboutTitle: "Behind the camera.<br>Connected to<br>your passion.",
  aboutDesc1:
    "I’m the filmmaker behind JBS Street Recordings, known as 側影之心. Based in Taiwan, I document dance and live performance, from K-pop covers on the street to school showcases and competitions.",
  aboutDesc2:
    "I look for the feeling within a movement, the connection on stage, and the moments that happen only once. So dancers can see their hard work, and more people can feel the passion behind it.",
  aboutLink: "More moments on Instagram",
  stat1: "YouTube subscribers",
  stat2: "Published videos",
  stat3: "Channel views",
  statsNote: "Public YouTube figures<br>As of September 9, 2026",
  processTitle:
    'From the first idea to pressing play<span class="accent">.</span>',
  process1Title: "Tell me about your performance",
  process1Desc:
    "Share the date, location and what you have in mind. We’ll start with your needs and check availability.",
  process2Title: "Find the right perspective",
  process2Desc:
    "We’ll discuss the schedule, camera positions and key moments, then agree on a quote, coverage and delivery before filming.",
  process3Title: "Keep the moment alive",
  process3Desc:
    "Your footage is prepared and delivered as agreed, ready to keep, share and watch again.",
  contactTitle: "Your next great moment.<br>Let’s capture it.",
  contactDesc:
    "A showcase, a performance, or a dance film in mind?<br>Bring your idea. Let’s talk.",
  contactButton: "Get in touch on Instagram",
  briefLabel: "LET’S START WITH YOUR IDEA",
  briefTitle: "A few things to start with:",
  brief1: "Your name or the name of your crew",
  brief2: "Date, location and performance duration",
  brief3: "What you need, references and budget",
  brief4: "Intended use and your delivery deadline",
  copyBrief: "Copy the project brief template",
  faqTitle: "Before we start filming",
  faq1Title: "How do I check availability and pricing?",
  faq1Desc:
    "Send an Instagram message with your date, location, duration and filming needs. Pricing depends on coverage, travel and delivery requirements. Bookings are subject to mutual confirmation.",
  faq2Title: "Can I request vertical video or original footage?",
  faq2Desc:
    "Let’s discuss the framing, camera positions, suitability of the footage and deliverables first. If you appear in a published video, send its link and your timestamps on Instagram. Original files are subject to availability.",
  faq3Title: "Will my video be published on YouTube?",
  faq3Desc:
    "We’ll agree on publication, intended use and performer permissions before the shoot. Let me know about any unreleased work, music usage restrictions or event requirements so we can plan accordingly.",
  footerTagline: "Keeping passion in the frame.",
  backTop: "Back to top ↑",
  watchYoutube: "Watch on YouTube ↗",
  playerNote: "If the player does not load, choose “Watch on YouTube”.",
};

const translatedElements = [...document.querySelectorAll("[data-i18n]")];
const chinese = Object.fromEntries(
  translatedElements.map((el) => [el.dataset.i18n, el.innerHTML]),
);
const imageDescriptions = [
  "Dancers performing under blue stage lights at SYM Dance30",
  "ICONIC BY MISTAKE, a dance pop-up in Taichung",
  "Hsin Sheng Dance performing at the Rïtmo showcase",
  "BOOMBAYAH dance cover at the Dance on Life competition",
  "Side-camera view of a TWICE Strategy cover in Xinyi",
  "Fireworks performing a KATSEYE GNARLY dance cover",
  "Yingge, Mingde, Songshan and Xiufeng performing JAZZ at Dance30",
  "The side-camera perspective and setting of the Strategy dance cover",
];
const siteImages = [...document.querySelectorAll("main img")];
const chineseImageDescriptions = siteImages.map((image) => image.alt);
const languageButton = document.querySelector(".language-toggle");
const menuButton = document.querySelector(".menu-toggle");
const mobileNav = document.querySelector(".mobile-nav");
const dialog = document.querySelector(".film-dialog");
const playerContainer = document.querySelector(".video-container");
let language = "zh";
let openedFilm = null;
let opener = null;

function setMenu(open) {
  mobileNav.hidden = !open;
  menuButton.setAttribute("aria-expanded", String(open));
  menuButton.setAttribute(
    "aria-label",
    language === "en"
      ? open
        ? "Close menu"
        : "Open menu"
      : open
        ? "關閉選單"
        : "開啟選單",
  );
}

function updateFilmCaption() {
  if (!openedFilm) return;
  const index = language === "en" ? 1 : 0;
  document.getElementById("film-title").textContent =
    films[openedFilm].title[index];
  document.getElementById("film-credit").textContent =
    films[openedFilm].credit[index];
}

function setLanguage(next) {
  language = next === "en" ? "en" : "zh";
  const copy = language === "en" ? english : chinese;
  for (const element of translatedElements) {
    if (copy[element.dataset.i18n] !== undefined)
      element.innerHTML = copy[element.dataset.i18n];
  }
  document.documentElement.lang = language === "en" ? "en" : "zh-Hant";
  siteImages.forEach((image, i) => {
    image.alt =
      language === "en" ? imageDescriptions[i] : chineseImageDescriptions[i];
  });
  document.title =
    language === "en"
      ? "JBS Street Recordings | Dance & Live Performance Filmmaker in Taiwan"
      : "側影之心 JBS Street Recordings｜舞蹈・現場演出・動態影像";
  document.querySelector('meta[name="description"]').content =
    language === "en"
      ? "Taiwan-based dance and live performance filmmaker. Explore K-pop covers, live showcases and competition films by JBS Street Recordings."
      : "側影之心 JBS Street Recordings，專注舞蹈、K-pop cover、舞展與賽事的動態影像紀錄。看看作品，聊聊你的下一場演出。";
  languageButton.textContent = language === "en" ? "中" : "EN";
  languageButton.setAttribute(
    "aria-label",
    language === "en" ? "切換繁體中文" : "Switch to English",
  );
  document
    .querySelector(".close-dialog")
    .setAttribute("aria-label", language === "en" ? "Close film" : "關閉影片");
  document
    .querySelector(".brand")
    .setAttribute(
      "aria-label",
      language === "en"
        ? "JBS Street Recordings home"
        : "側影之心 JBS Street Recordings 首頁",
    );
  document
    .querySelector(".desktop-nav")
    .setAttribute(
      "aria-label",
      language === "en" ? "Main navigation" : "主要導覽",
    );
  mobileNav.setAttribute(
    "aria-label",
    language === "en" ? "Mobile navigation" : "行動版導覽",
  );
  document
    .querySelector(".filters")
    .setAttribute(
      "aria-label",
      language === "en" ? "Filter films" : "作品分類",
    );
  document
    .querySelector(".brief-fallback")
    .setAttribute(
      "aria-label",
      language === "en" ? "Project brief template" : "合作需求範本",
    );
  document.querySelectorAll("[data-video]").forEach((link) => {
    const title = films[link.dataset.video].title[language === "en" ? 1 : 0];
    link.setAttribute(
      "aria-label",
      `${language === "en" ? "Play" : "播放"} ${title}`,
    );
  });
  document
    .querySelectorAll(".service-arrow")
    .forEach((link, i) =>
      link.setAttribute(
        "aria-label",
        language === "en"
          ? `Enquire about ${english[`service${i + 1}Title`]}`
          : `洽詢${chinese[`service${i + 1}Title`]}`,
      ),
    );
  document.querySelector(".copy-status").textContent = "";
  document.querySelector(".brief-fallback").hidden = true;
  setMenu(false);
  updateFilmCaption();
  try {
    localStorage.setItem("jbs-language", language);
  } catch {
    /* The page also works without browser storage. */
  }
}

languageButton.hidden = false;
menuButton.hidden = false;
languageButton.addEventListener("click", () =>
  setLanguage(language === "zh" ? "en" : "zh"),
);
menuButton.addEventListener("click", () => setMenu(mobileNav.hidden));
mobileNav.addEventListener("click", (event) => {
  if (event.target.closest("a")) setMenu(false);
});
document.addEventListener("click", (event) => {
  if (!event.target.closest(".site-header") && !mobileNav.hidden)
    setMenu(false);
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !mobileNav.hidden) {
    setMenu(false);
    menuButton.focus();
  }
});
matchMedia("(min-width: 761px)").addEventListener("change", (event) => {
  if (event.matches) setMenu(false);
});

const filters = document.querySelector(".filters");
filters.hidden = false;
filters.addEventListener("click", (event) => {
  const button = event.target.closest("[data-filter]");
  if (!button) return;
  filters
    .querySelectorAll("button")
    .forEach((item) =>
      item.setAttribute("aria-pressed", String(item === button)),
    );
  let count = 0;
  document.querySelectorAll(".work-card").forEach((card) => {
    const show =
      button.dataset.filter === "all" ||
      card.dataset.category === button.dataset.filter;
    card.hidden = !show;
    if (show) count++;
  });
  document.querySelector(".work-count").textContent =
    `${String(count).padStart(2, "0")} ${count === 1 ? "FILM" : "FILMS"}`;
});

document.querySelectorAll("[data-video]").forEach((link) => {
  link.addEventListener("click", (event) => {
    // Preserve normal link behavior for new-tab gestures and older browsers.
    if (
      event.ctrlKey ||
      event.metaKey ||
      event.shiftKey ||
      event.altKey ||
      typeof dialog.showModal !== "function"
    )
      return;
    const id = link.dataset.video;
    if (!films[id]) return;
    event.preventDefault();
    openedFilm = id;
    opener = link;
    updateFilmCaption();
    document.querySelector(".video-external").href =
      `https://www.youtube.com/watch?v=${id}`;
    const iframe = document.createElement("iframe");
    iframe.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&playsinline=1`;
    iframe.title = films[id].title[language === "en" ? 1 : 0];
    iframe.allow =
      "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    iframe.allowFullscreen = true;
    iframe.referrerPolicy = "strict-origin-when-cross-origin";
    playerContainer.replaceChildren(iframe);
    dialog.showModal();
    document.body.classList.add("modal-open");
    document.querySelector(".close-dialog").focus();
  });
});
document
  .querySelector(".close-dialog")
  .addEventListener("click", () => dialog.close());
dialog.addEventListener("click", (event) => {
  if (event.target !== dialog) return;
  const rect = dialog.getBoundingClientRect();
  if (
    event.clientX < rect.left ||
    event.clientX > rect.right ||
    event.clientY < rect.top ||
    event.clientY > rect.bottom
  )
    dialog.close();
});
dialog.addEventListener("close", () => {
  playerContainer.replaceChildren();
  document.body.classList.remove("modal-open");
  openedFilm = null;
  opener?.focus({ preventScroll: true });
});

const copyButton = document.querySelector(".copy-brief");
copyButton.hidden = false;
copyButton.addEventListener("click", async () => {
  const text =
    language === "en"
      ? "Hi JBS! I’d like to discuss a filming project.\n\nName / crew:\nDate & location:\nPerformance / coverage duration:\nFilming needs:\nReference video:\nBudget:\nIntended use (YouTube / Instagram / private):\nPreferred delivery date:\n"
      : "你好，側影之心！我想洽詢拍攝合作。\n\n姓名／團隊名稱：\n活動日期與地點：\n演出／拍攝時長：\n希望拍攝的內容：\n參考影片：\n預算範圍：\n預計用途（YouTube／IG／私人留存）：\n希望收到影片的日期：\n";
  const status = document.querySelector(".copy-status");
  const fallback = document.querySelector(".brief-fallback");
  try {
    await navigator.clipboard.writeText(text);
    fallback.hidden = true;
    status.textContent =
      language === "en"
        ? "Copied. Paste into an Instagram message and fill in your details."
        : "已複製！貼到 Instagram 私訊，填入你的需求就可以了。";
  } catch {
    fallback.value = text;
    fallback.hidden = false;
    fallback.focus();
    fallback.select();
    status.textContent =
      language === "en"
        ? "Select and copy the template below, then paste it into Instagram."
        : "請選取下方範本並複製，再貼到 Instagram 私訊。";
  }
});

let initialLanguage = new URLSearchParams(location.search).get("lang");
if (!initialLanguage) {
  try {
    initialLanguage = localStorage.getItem("jbs-language");
  } catch {
    /* Default to Traditional Chinese. */
  }
}
setLanguage(initialLanguage);
document.getElementById("year").textContent = String(new Date().getFullYear());
