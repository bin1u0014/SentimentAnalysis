"""전체 데이터 수집 파이프라인 — 하루 한 번 실행"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from yfinance_collector import collect_prices
from finnhub_collector import collect_news
from rss_collector import collect_rss
from datetime import datetime

def run_pipeline():
    print(f"\n{'='*50}")
    print(f"데이터 수집 시작: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*50}\n")
    
    print("[1/3] 주가 데이터 수집...")
    collect_prices()
    
    print("\n[2/3] Finnhub 뉴스 수집...")
    collect_news()
    
    print("\n[3/3] RSS 뉴스 수집...")
    collect_rss()
    
    print(f"\n{'='*50}")
    print("전체 수집 완료!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_pipeline()