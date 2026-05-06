!pip install requests
import requests
url="http://localhost:8055/items/petshop"
response=requests.get(url)

if response.status_code==200:
    articles=response.json()["data"]
    for a in articles:
        print(a["title"])