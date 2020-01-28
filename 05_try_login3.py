import requests

session = requests.session()

post_url = "http://www.renren.com/PLogin.do"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
          "Referer": "http://www.renren.com/972693684/newsfeed/photo"
          }
post_data = {"email":"mr_mao_hacker@163.com","password":"alarmchime"}
#post_data = {"email":"1134231904",
 #            "password":"123.jr.uu.n.qq"}
session.post(post_url,headers=header,data=post_data)

url = "http://www.renren.com/972693684/profile"
response  = session.get(url,headers=header)
with open("renren4.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())


