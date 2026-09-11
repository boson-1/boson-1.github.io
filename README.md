# 側影之心 · JBS Street Recordings

舞蹈、街頭演出與舞展賽事的個人動態影像作品集。

**正式網站：<https://yt.jamesboson.com/>**

GitHub Pages 從 `main` 分支根目錄發布；`CNAME` 保留原有自訂網域。

## 本機預覽

發布結果是靜態 HTML，不需要前端框架。預覽現成頁面，在專案根目錄執行：

```sh
python -m http.server 4173 --bind 127.0.0.1
```

開啟 <http://127.0.0.1:4173/>。修改內容後，使用 Python 3 與 Node.js（僅標準函式庫，無需 npm/pip 套件）重新產生並檢查：

```sh
python scripts/build-site.py
python scripts/check-site.py
node --check app.js
node --check analytics.js
```

## 維護內容

- `templates/home.html`：首頁繁體中文內容與結構的來源。
- `index.html`、`en/index.html`：產生的中英文首頁；不要直接修改，避免下次建置覆蓋。
- `films/`、`en/films/`：產生的 12 支作品中英文觀看頁。
- `content/video-metadata.json`：經核對的 YouTube 發布時間、影片秒數與來源；發布日期不等於演出日期。
- `scripts/build-site.py`：產生 26 個靜態頁、canonical、hreflang、結構化資料與含影片資訊的網站地圖。
- `scripts/check-site.py`：檢查不執行 JavaScript 時的內容、連結、語言、影片標記與 Sitemap。
- `film.css`：作品觀看頁的響應式排版。
- `styles.css`：桌面、平板、手機排版及減少動態效果設定。
- `app.js`：英文文案、作品資料、分類、影片燈箱、語言連結、手機選單、合作需求範本。
- `analytics.js`：GA4 與 Cloudflare Web Analytics，僅正式網域啟用；首頁與 404 頁共用。
- `assets/images/`：頻道真實公開影片縮圖，僅轉為 WebP。沒有使用外部攝影師的作品素材。
- `docs/research.md`：設計參考、頻道內容依據與作品來源。

新增影片時，同步更新 `templates/home.html` 作品卡片、`app.js` 的 `films` 與 `english`，並補上 `content/video-metadata.json`，再執行建置。中文文案在模板；英文對照位於 `english`，圖片英文替代文字位於模板的 `data-alt-en`。資料更新後，將建置腳本的 `UPDATED` 改為實際內容更新日期；不要每次重建就刷新日期。移除作品時也需移除對應中英文輸出目錄，再更新檢查腳本的頁數斷言。

繁體中文網址為 `/`，英文為 `/en/`，兩者皆有完整靜態內容。語言連結會切換網址，不再依 localStorage 自動改寫首頁語言。舊 `?lang=en`、`?lang=zh` 網址會透過 JavaScript 轉往對應語言，保留其他查詢參數與錨點。GitHub Pages 沒有伺服器重新導向規則；canonical 與 Sitemap 只列正式網址。

公開頻道數據的擷取日期為 **2026-09-09**，不是即時統計。更新時也請同步修改資料日期。首頁下修顯示為 44K+ 訂閱者、1,900+ 影片、11M+ 次觀看。

作品順序固定為「舞展/成發」、「賽事記錄」、「KPOP 快閃」，目前共 12 支（6 / 4 / 2）。KPOP 快閃僅收錄原始標題以 `[KPOP IN PUBLIC]` 開頭的影片，按公開觀看數取前二。`films` 的 `sourceTitle`、`viewCount` 與 `viewsCheckedAt` 保存此次核對資料。Banner 與分享圖使用頻道觀看最高的 BOOMBAYAH，並顯示 200 萬觀看 UP。

## 行為與發布

- 首頁影片在使用者點擊後才載入 YouTube 隱私增強模式播放器；關閉燈箱會移除 iframe 並停止播放。作品卡片底層連結指向站內觀看頁，燈箱另有「作品詳細資料」連結。
- 獨立作品頁在 HTML 中直接提供單一 YouTube 隱私增強模式播放器，無需點擊才建立 iframe，影片不自動播放。這讓爬蟲可辨識影片，也會在進入作品頁時載入 YouTube。每頁保留 YouTube 原片連結。
- 停用 JavaScript 時，中英文服務、作品與觀看頁仍可閱讀，語言連結仍可使用。
- Instagram 是公開合作聯絡管道。複製範本只會寫入使用者的剪貼簿，不會代為傳送訊息；若剪貼簿被瀏覽器阻擋，會顯示可自行複製的文字框。
- 使用 GA4 統計瀏覽及作品互動、Cloudflare Web Analytics 統計流量與載入效能。沒有假聯絡表單、訂閱流程或後端；交付規格、價格、檔期均以個別合作確認為準。
- PAT 與驗證設定不在專案內；不要把憑證寫進 HTML、Git remote URL 或任何提交檔案。

將變更提交並推送到 `main` 後，GitHub Pages 會自動發布。可在儲存庫 Pages 設定與 Actions 查看建置結果。原始連結頁仍可由 Git 歷史的 `72f7d8e` 還原。

## 搜尋最佳化（2026-09-12）

- 以台灣舞蹈錄影、舞蹈教室成果發表、高中職聯合成發、賽事記錄和 KPOP 快閃為內容主題。尚未確認特定城市的接案範圍，沒有加入實體地址、虛構商家、價格或評論。
- 中英文有自己的 canonical，透過 `zh-Hant`、`en`、`x-default` 互相連結；所有語言皆由 HTML 直接提供。首頁保留原先分享用影片縮圖。
- 以 `Person`、`WebSite`、`CollectionPage`、`ItemList` 描述品牌與作品，取代缺少實體商家資訊的 `ProfessionalService`。觀看頁使用 `VideoObject` 與 `BreadcrumbList`，資料與可見內容一致。
- 一般 Sitemap 共 26 頁，包含 24 個影片項目。`robots.txt` 允許搜尋公開頁面及資源，排除維護用資料夾。404 保持 HTTP 404 與 noindex。
- 首頁與作品頁的 JS/CSS 使用內容雜湊版本，避免新版 HTML 配到舊版作品程式。首頁沿用 WebP、首圖優先下載、非首圖延遲載入與預留圖片尺寸。觀看頁預留播放器比例。
- [Search Console](https://search.google.com/search-console?resource_id=https%3A%2F%2Fyt.jamesboson.com%2F) 是索引、搜尋字詞、曝光與點擊的追蹤工具；GA4 負責進站互動，Cloudflare 負責載入效能。沒有保證索引、名次、影片縮圖或 AI 引用。
- 官方依據與本次驗證詳見 `docs/seo-2026.md`。

## 網站分析

2026-09-11 建立與安裝：

- [GA4 報表](https://analytics.google.com/analytics/web/#/a257713851p553752858/reports/intelligenthome)：資源「側影之心 · JBS Street Recordings」，台灣時區／新台幣，評估 ID `G-HQ7TTCGWDC`，網站串流 ID `15761110780`。
- [Cloudflare Web Analytics](https://dash.cloudflare.com/e0aadeb53cd57382409c807f17c6eadf/web-analytics)：主機 `yt.jamesboson.com`，手動安裝官方 module beacon；網站繼續使用 GitHub Pages。
- 兩項分析僅在 `yt.jamesboson.com` 啟動，本機預覽不傳送資料。Cloudflare 的 SPA 自動追蹤已關閉，避免單頁作品集的頁內切換被算成新頁面。
- GA4 開啟加強型評估；程式另外傳送 `film_open`（`video_id`、`placement`）、`work_filter`（`work_category`）、`contact_click`（`contact_method`、`placement`），三者皆附 `site_language`。`film_open` 表示使用者點擊作品，不代表已開始觀看。Instagram 點擊也不代表已送出合作訊息。
- 自訂事件只取公開影片 ID、分類及固定介面位置；不讀取剪貼簿或合作需求內容。GA 廣告個人化與 Google signals 已關閉。GA 的一般分析 cookie 與來源／裝置統計仍依官方代碼運作。
- 評估 ID 和 Cloudflare beacon token 是公開網站識別碼，不是後台 API 密鑰。不要另外加入相同代碼或開啟 Cloudflare 自動注入，以免重複統計。
- 一般報表需要處理時間，可先用 GA4 即時報表及 Cloudflare 的短時間範圍檢查。資料從安裝後開始累積，沒有歷史流量回補。

官方安裝文件：[Google tag](https://developers.google.com/tag-platform/gtagjs)、[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)。
