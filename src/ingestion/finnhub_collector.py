"""Finnhub 뉴스 수집"""
import finnhub
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

TICKERS = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN"]

def collect_news(days_back=7):
    api_key = os.getenv("FINNHUB_API_KEY")
    if not api_key:
        raise ValueError("FINNHUB_API_KEY가 .env에 없어요!")
    
    client = finnhub.Client(api_key=api_key)
    
    end = datetime.today()
    start = end - timedelta(days=days_back)
    end_str = end.strftime("%Y-%m-%d")
    start_str = start.strftime("%Y-%m-%d")
    
    all_news = []
    for ticker in TICKERS:
        print(f"{ticker} 뉴스 수집 중...")
        news = client.company_news(ticker, _from=start_str, to=end_str)
        for item in news:
            item["ticker"] = ticker
            item["source"] = "finnhub"
        all_news.extend(news)
        print(f"  → {len(news)}개 기사")
    
    os.makedirs("data/raw", exist_ok=True)
    path = f"data/raw/finnhub_{datetime.today().strftime('%Y-%m-%d')}.json"
    with open(path, "w") as f:
        json.dump(all_news, f, indent=2)
    print(f"저장 완료: {path} (총 {len(all_news)}개)")
    return all_news

if __name__ == "__main__":
    collect_news()