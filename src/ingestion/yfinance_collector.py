"""주가 데이터 수집 — yfinance"""
import yfinance as yf
import pandas as pd
from datetime import datetime
import os

TICKERS = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN", "SPY"]

def collect_prices(start="2020-01-01", end=None):
    if end is None:
        end = datetime.today().strftime("%Y-%m-%d")
    
    print(f"주가 데이터 수집 중: {TICKERS}")
    df = yf.download(TICKERS, start=start, end=end, auto_adjust=True)
    
    os.makedirs("data/raw", exist_ok=True)
    path = f"data/raw/prices_{datetime.today().strftime('%Y-%m-%d')}.parquet"
    df.to_parquet(path)
    print(f"저장 완료: {path} ({len(df)}행)")
    return df

if __name__ == "__main__":
    collect_prices()