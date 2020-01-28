import requests
url = "https://fanyi.baidu.com/basetrans"
query_response = {"query": "人生苦短，我用python",
                  "from": "zh",
                  "to": "en"}
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "referer": "https://fanyi.baidu.com/?aldtype=16047"}
response = requests.post(url,data=query_response,headers=headers,timeout=3)
print(response)

print(response.content.decode())

print("response.url:    "+str(response.url))
print("response.request.url:    "+str(response.request.url))
print("response.request.headers:    "+str(response.request.headers))
print("response.headers:    "+str(response.headers))