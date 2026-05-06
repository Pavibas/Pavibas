import requests

def get_data():
    url="https://jsonplaceholder.typicode.com/posts/1"
    response=requests.get(url)
    return response.json()

if __name__=="___main___":
    print(get_data())