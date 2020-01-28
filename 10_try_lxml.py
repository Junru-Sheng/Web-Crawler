import requests
from lxml import etree
import json
url = "https://movie.douban.com/chart"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
           }
response = requests.get(url,headers=headers)
html_str = response.content.decode()
#print(html_str)
#使用lxml方法提取数据
html = etree.HTML(html_str)
'''
#print(html)
print("Movie's href:")
url_list = html.xpath("//div[@class='indent']//table//div[@class='pl2']/a/@href")
print(url_list)
print("\n")
print("Movie's image:")

img_list = html.xpath("//div[@class='indent']/div/table//tr[@class='item']/td[1]/a[@class='nbg']/img/@src")
print(img_list)
'''
ret = html.xpath("//div[@class='indent']//table")
#print(ret)
num = 0
for table in ret:
    item = {}
    num += 1
    item["title"] = table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()
    item["href"] = table.xpath(".//a[@class='nbg']/img/@src")[0]
    item["comment_num"] = table.xpath(".//div[@class='star clearfix']/span[@class='pl']/text()")[0]
    item["rating_nums"] = table.xpath(".//div[@class='star clearfix']/span[@class='rating_nums']/text()")[0]
    '''
    with open("影评.txt",'a',encoding='utf-8') as f:
        f.write(str(num) +':'+ '\t')
        for k,v in item.items():
            f.write(k+':')
            f.write(str(v)+'\t')
        f.write('\n')
    '''
    #Save as json document
    with open("影评.json", 'a', encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False))
        f.write('\n')