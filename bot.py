import requests
from telegram import Bot
from datetime import datetime
import asyncio
import time
import xml.etree.ElementTree as ET

TOKEN = "8640244328:AAEme0Ynla9S0dROqJNBs114x_Z_-XNlPF4"
CHAT_ID = 7267064983

def get_tech_news():
    url = "https://news.google.com/rss/search?q=technology"
    response = requests.get(url)
    
    root = ET.fromstring(response.content)
    items = root.findall(".//item")[:5]

    news_text = f"📰 Tech News - {datetime.now().strftime('%Y-%m-%d')}\n\n"

    for item in items:
        title = item.find("title").text
        link = item.find("link").text
        news_text += f"🔹 {title}\n{link}\n\n"

    return news_text

async def send_news():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=get_tech_news())

# loop كل 24 ساعة
while True:
    asyncio.run(send_news())
    print("✅ News sent")
    time.sleep(86400)  # 24h