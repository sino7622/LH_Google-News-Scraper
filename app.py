from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib3
import traceback
from email.utils import parsedate_to_datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    query = request.args.get('q', '')
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')

    search_query = query
    if start_date: search_query += f" after:{start_date}"
    if end_date:   search_query += f" before:{end_date}"
    
    encoded_query = urllib.parse.quote(search_query)
    rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(rss_url, headers=headers, timeout=15, verify=False)
        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all('item')
        
        news_data = []
        for item in items:
            raw_date = item.pubDate.get_text() if item.pubDate else ""
            formatted_date = "0000-00-00 00:00:00" # 預設值，方便排序
            
            if raw_date:
                try:
                    dt = parsedate_to_datetime(raw_date)
                    formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    pass

            news_data.append({
                'title': item.title.get_text() if item.title else "無標題",
                'summary': item.description.get_text() if item.description else "無摘要",
                'link': item.link.get_text() if item.link else "#",
                'pubDate': formatted_date,
                'source': item.source.get_text() if item.source else "未知來源"
            })

        # --- 核心更新：按發佈日期從新到舊排序 ---
        news_data.sort(key=lambda x: x['pubDate'], reverse=True)
        # ------------------------------------

        return jsonify(news_data)
    except Exception as e:
        traceback.print_exc() 
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)