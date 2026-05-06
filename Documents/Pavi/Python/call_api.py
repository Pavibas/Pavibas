import requests

url="https://apiurl"

response=requests.get(url)

print(response.status_code)
print(response.json())