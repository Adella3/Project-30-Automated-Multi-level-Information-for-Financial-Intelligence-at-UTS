# The Guardian API - Industry Level News Collection

import requests
from datetime import datetime

API_KEY = "68ccc338-0ad3-475e-875d-f30696608dc7"

# Industry Level - example
industries = [
    "semiconductor industry",  
    "banking sector",          
    "EV automotive industry"   
]

# Date filtering - after 2022
for industry in industries:
    url = "https://content.guardianapis.com/search"
    
    params = {
        "q": industry,
        "from-date": "2022-01-01",
        "to-date": "2026-12-31",
        "lang": "en",
        "order-by": "newest",
        "show-fields": "headline,bodyText",
        "api-key": API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    print(f"\n=== {industry} News ===")
    articles = data['response']['results']
    
    for article in articles[:2]:
        print("Title:", article['webTitle'])
        print("Date:", article['webPublicationDate'][:10])
        print("URL:", article['webUrl'])
        print("---")
