"""Google News RSS 수집 — API 키 불필요"""
import feedparser
import json
import os
from datetime import datetime

QUERIES = [
    "AAPL Apple stock",
    "TSLA Tesla stock",
    "MSFT Microsoft stock",
    "GOOGL Google stock",
    "AMZN Amazon stock",
    "stock market today",
]

def collect_rss():
    all_articles = []
    
    for query in QUERIES:
        url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            all_articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", ""),
                "link": entry.get("link", ""),
                "query": query,
                "source": "google_rss"
            })
        print(f"'{query}' → {len(feed.entries)}개")
    
    os.makedirs("data/raw", exist_ok=True)
    path = f"data/raw/rss_{datetime.today().strftime('%Y-%m-%d')}.json"
    with open(path, "w") as f:
        json.dump(all_articles, f, indent=2, ensure_ascii=False)
    print(f"저장 완료: {path} (총 {len(all_articles)}개)")
    return all_articles

if __name__ == "__main__":
    collect_rss()