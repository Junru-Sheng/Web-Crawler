import json
import requests

url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1572416741143"
headers = {
    "Referer": "https://m.douban.com/tv/american",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
response = requests.get(url,headers=headers)
json_str = response.content.decode()
print(json_str)
ret1 = json.loads(json_str)
print(type(ret1))

with open("douban.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=2))