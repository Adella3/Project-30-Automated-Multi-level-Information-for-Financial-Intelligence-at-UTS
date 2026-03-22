# Yahoo Finance API - Entity Level News Collection

import yfinance as yf
from datetime import datetime

# Entity Level - example
entities = ["AAPL", "TSLA", "MSFT"]

# Date filtering - after 2022
start_date = datetime(2022, 1, 1)
end_date = datetime(2026, 12, 31)

for symbol in entities:
    ticker = yf.Ticker(symbol)
    news = ticker.news

    print(f"\n=== {symbol} News ===")

    count = 0
    for article in news:
        pub_date = datetime.strptime(
            article['content']['pubDate'][:10], "%Y-%m-%d"
        )

        if start_date <= pub_date <= end_date:
            print("Title:", article['content']['title'])
            print("Date:", article['content']['pubDate'][:10])
            print("Source:", article['content']['provider']['displayName'])
            print("URL:", article['content']['canonicalUrl']['url'])
            print("---")
            count += 1
            if count == 2:
                break