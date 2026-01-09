📰 Google News 進階檢索與 Excel 匯出系統這是一個基於 Python Flask 開發的輕量化 Web 工具，旨在幫助使用者透過 Google News RSS 進行精準的新聞檢索。系統支援 Google 原生的高級搜尋運算子，並能將檢索結果一鍵匯出為結構化的 Excel 報表，非常適合輿情分析、資料收集與日報整理。✨ 功能亮點精準指令搜尋：支援 intitle:、site:、""、- 等高級搜尋指令，讓檢索結果更精確。日期範圍篩選：結合 Google 的 after: 與 before: 語法，精確鎖定特定時間區間的新聞。時間排序優化：搜尋結果自動按發佈時間 從新到舊 排序。格式化日期：發佈時間統一轉換為 年-月-日 時:分:秒。Excel 智慧命名：下載的檔名會自動帶入「關鍵字」與「搜尋起訖日期」，方便檔案管理。純淨資料：自動清除新聞摘要中的 HTML 標籤，確保匯出的資料乾淨整齊。SSL 豁免機制：內建 SSL 驗證跳過功能，確保在公司或組織內網環境下也能穩定連線。🚀 快速開始1. 環境需求Python 3.8+Git2. 安裝步驟Bash# 複製專案
git clone https://github.com/你的帳號/你的專案名稱.git
cd 你的專案名稱

# 建立虛擬環境
python -m venv .venv

# 啟動虛擬環境 (Windows)
.\.venv\Scripts\activate

# 安裝必要套件
pip install -r requirements.txt
3. 執行程式Bashpython app.py
啟動後，在瀏覽器輸入 http://127.0.0.1:5000 即可開始使用。💡 Google 搜尋指令指南本系統直接支援 Google 原生搜尋語法，您可以直接在關鍵字欄位輸入以下指令：指令名稱範例效果說明精準比對"沙崙農場"必須完全符合括號內的字串順序。限定標題intitle:光電只在新聞標題中尋找關鍵字。排除字詞沙崙 -光電搜尋結果中不得出現「光電」一詞。指定媒體site:ltn.com.tw只搜尋特定網站（如自由時報）。或 (OR)台南 OR 高雄包含其中一個詞彙即可。邏輯分組(台南 OR 高雄) 沙崙搜尋包含沙崙，且地點在台南或高雄的新聞。📂 檔案結構Plaintext.
├── app.py              # Flask 後端邏輯 (處理 RSS 抓取與日期轉換)
├── templates/
│   └── index.html      # 前端介面 (搜尋指令、表格顯示與 Excel 匯出)
├── .gitignore          # 排除不需要上傳的檔案 (如 .venv, .xlsx)
└── requirements.txt    # 套件依賴清單
🌐 線上部署 (以 Render 為例)本專案已針對線上部署進行優化：Build Command: pip install -r requirements.txtStart Command: gunicorn app:app注意：部署至線上環境時，請確保 requirements.txt 中包含 gunicorn。🛠 使用技術Backend: Python FlaskFrontend: Bootstrap 5, JavaScript (Fetch API)Library: BeautifulSoup4 (XML Parsing), SheetJS (Excel Export)