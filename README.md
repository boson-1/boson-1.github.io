# 側影之心 · JBS Street Recordings

舞蹈、街頭演出與舞展賽事的個人動態影像作品集。

**正式網站：<https://yt.jamesboson.com/>**

GitHub Pages 從 `main` 分支根目錄發布；`CNAME` 保留原有自訂網域。

## 本機預覽

不需要安裝前端依賴或建置工具。在專案根目錄執行：

```sh
python -m http.server 4173 --bind 127.0.0.1
```

開啟 <http://127.0.0.1:4173/>。語法檢查：`node --check app.js`。

## 維護內容

- `index.html`：預設繁體中文、精選作品、服務、合作資訊、SEO metadata 與結構化資料。
- `styles.css`：桌面、平板、手機排版及減少動態效果設定。
- `app.js`：英文文案、作品資料、分類、影片燈箱、語言記憶、手機選單、合作需求範本。
- `analytics.js`：GA4 與 Cloudflare Web Analytics，僅正式網域啟用；首頁與 404 頁共用。
- `assets/images/`：頻道真實公開影片縮圖，僅轉為 WebP。沒有使用外部攝影師的作品素材。
- `docs/research.md`：設計參考、頻道內容依據與作品來源。

新增影片時，同步更新 HTML 作品卡片與 `app.js` 的 `films`。更新中文文案請修改 HTML；英文對照位於 `english`，圖片英文替代文字位於 HTML 的 `data-alt-en`。`?lang=en`、`?lang=zh` 可指定語言；一般瀏覽會記住手動選擇。

公開頻道數據的擷取日期為 **2026-09-09**，不是即時統計。更新時也請同步修改資料日期。首頁下修顯示為 44K+ 訂閱者、1,900+ 影片、11M+ 次觀看。

作品順序固定為「舞展/成發」、「賽事記錄」、「KPOP 快閃」，目前共 12 支（6 / 4 / 2）。KPOP 快閃僅收錄原始標題以 `[KPOP IN PUBLIC]` 開頭的影片，按公開觀看數取前二。`films` 的 `sourceTitle`、`viewCount` 與 `viewsCheckedAt` 保存此次核對資料。Banner 與分享圖使用頻道觀看最高的 BOOMBAYAH，並顯示 200 萬觀看 UP。

## 行為與發布

- 影片在使用者點擊後，才載入 YouTube 隱私增強模式播放器；關閉燈箱會移除 iframe 並停止播放。每支影片保留直接前往 YouTube 的連結。
- 停用 JavaScript 時，服務與作品內容仍可閱讀，影片連結仍可使用。
- Instagram 是公開合作聯絡管道。複製範本只會寫入使用者的剪貼簿，不會代為傳送訊息；若剪貼簿被瀏覽器阻擋，會顯示可自行複製的文字框。
- 使用 GA4 統計瀏覽及作品互動、Cloudflare Web Analytics 統計流量與載入效能。沒有假聯絡表單、訂閱流程或後端；交付規格、價格、檔期均以個別合作確認為準。
- PAT 與驗證設定不在專案內；不要把憑證寫進 HTML、Git remote URL 或任何提交檔案。

將變更提交並推送到 `main` 後，GitHub Pages 會自動發布。可在儲存庫 Pages 設定與 Actions 查看建置結果。原始連結頁仍可由 Git 歷史的 `72f7d8e` 還原。

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
