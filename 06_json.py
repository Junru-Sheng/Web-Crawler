# coding=utf-8
import requests
import json
url = "http://m.youdao.com/translate"
print("-----欢迎来到有道翻译------")
quary_str = input("请输入想翻译的中文：   ")
data = {"inputtext": "你好，世界",
        "type": "AUTO"}

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
response = requests.post(url,data=data,headers=headers)
html_str = response.content.decode()
print(html_str)
#print(response.content.decode())
#dict_json = json.loads(html_str)
#print(dict_json)