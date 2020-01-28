import requests

url = "http://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
           }
response = requests.get(url,headers=headers,timeout=3)
'''获取网页的html字符串，第一种方法
#编码格式utf-8
response.encoding = "utf-8"
#print(response)
print(response.text)
'''
#第二种方法
#response.content获取二进制字节流转化为str形式，加上decode（）可以让中文自然地显示出来
#print(response.content.decode())

print(response.content.decode())