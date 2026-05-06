import requests
import json

url=""

json_str=json.dumps({
    "text": "",
    "message": [
        ""
    ]
})

headers={"x-api-key":"",
         "content-type": "application/json"}

response=requests.request("POST", url, headers=headers,data=json_str)
print(response.text)