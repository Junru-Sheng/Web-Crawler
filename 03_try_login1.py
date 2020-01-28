
import requests

url = "http://www.renren.com/972693684/profile"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
          "Referer": "http://www.renren.com/972693684/newsfeed/photo",
          "Cookie": "anonymid=k2bpy334-q9qq7m; depovince=LN; _r01_=1; JSESSIONID=abcYfYZv6_uv2cLJsgx4w; ick_login=17f7ccdb-2ca9-4462-a476-8bdfbd7e45d5; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; t=5b7f9cb8c6260a68b6b3a68dbb5dfb104; societyguester=5b7f9cb8c6260a68b6b3a68dbb5dfb104; id=972693684; xnsid=e8e503e6; jebecookies=23f0b57b-b5d2-43b8-87d7-0b33e2ae5f13|||||; ver=7.0; loginfrom=null; jebe_key=3f4272d7-c7bc-4249-852d-4751b467a3bd%7C502ef521ff6e226406ecdbabdf1a36e8%7C1572345677126%7C1%7C1572345673110; jebe_key=3f4272d7-c7bc-4249-852d-4751b467a3bd%7C502ef521ff6e226406ecdbabdf1a36e8%7C1572345677126%7C1%7C1572345673120; wp_fold=0"
          }

response = requests.get(url,headers=header)

with open("renren2.html","w",encoding="utf_8") as f:
    f.write(response.content.decode())
