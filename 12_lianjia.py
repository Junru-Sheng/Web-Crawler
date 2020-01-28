# -*- coding: utf-8 -*-

"""
@author: Junru Sheng
--------------------------------
@contact: junru.mail.dlut.edu.cn
--------------------------------
@Created on: 2019/11/20 14:26
"""
import requests
from retrying import retry
from lxml import etree
import csv
import os
def list_add_str(str0,list):
    return map(lambda x: str0+x, list)

class LianjiaSpyder:
    def __init__(self):
        self.url = "https://sh.lianjia.com/zufang/pg{}"
        self.headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                        }

    def get_urllist(self):
        url_list = [self.url.format(i) for i in range(0,101)]###可修改信息范围
        return url_list

    @retry(stop_max_attempt_number=3)
    def _parse(self,url):
        response = requests.get(url, headers=self.headers, timeout=30)
        return response.content.decode()

    def parse(self,url):
        try:
            html_str = self._parse(url)
        except:
            html_str = None
        return html_str

    def get_html_content(self,html_str):
        html = etree.HTML(html_str)
        href_list = html.xpath('//div[@class="content__list"]/div[@class="content__list--item"]/a/@href')
        href_list = list(list_add_str('https://sh.lianjia.com',href_list))
        #print(href_list)
        house_list = []
        num = 0
        count = 0
        house_quyu = html.xpath("//div[@class='content__list--item--main']/p[@class='content__list--item--des']/a[1]/text()")
        house_dizhi = html.xpath("//div[@class='content__list--item--main']/p[@class='content__list--item--des']/a[2]/text()")
        house_xiaoqu = html.xpath("//div[@class='content__list--item--main']/p[@class='content__list--item--des']/a[3]/text()")
        for url in href_list:
            #获取具体房子信息
            count += len(href_list)
            html_house = etree.HTML(self.parse(url))
            house_dict = {}
            house_dict["区域"] = house_quyu[num]
            house_dict["地址"] = house_dizhi[num]
            house_dict["小区"] = house_xiaoqu[num]
            house_dict["租金(元/月)"] = ''.join(html_house.xpath("//div[@class='content clear w1150']/div[@id='aside']/p[@class='content__aside--title']/span/text()"))
            house_dict["租赁方式"] = ''.join(html_house.xpath("//p[@class='content__article__table']/span[1]/text()"))
            house_dict["户型"] = ''.join(html_house.xpath("//p[@class='content__article__table']/span[2]/text()"))
            house_dict["面积"] = ''.join(html_house.xpath("//p[@class='content__article__table']/span[3]/text()"))
            house_dict["朝向"] = ''.join(html_house.xpath("//p[@class='content__article__table']/span[4]/text()"))
            house_dict["基本信息"] = html_house.xpath("//div[@class='content__article fl']/div[@class='content__article__info']/ul/li/text()")[1:]
            house_dict["图片链接"] = ''.join(html_house.xpath("//div[@class='content__article__slide__item']/img/@src"))
            house_dict["房源描述"] = ''.join(html_house.xpath("//div[@class='content__article__info3']/ul/li/p/@data-desc"))
            num += 1
            #print(house_dict)
            house_list.append(house_dict)
        print(house_list)
        print("房屋列表信息长度为{}".format(count))
        return house_list

    def save_file(self,house_list):
        #学学怎么写的，新手
        fieldnames = {'区域', '地址', '小区', '租金(元/月)', '租赁方式', '户型', '面积', '朝向', '基本信息', '图片链接', '房源描述'}
        # 第一次打开文件时，第一行写入表头
        if not os.path.exists("lianjia.csv"):
            with open("lianjia.csv", "w", newline='', encoding='utf-8') as csvfile:  # newline='' 去除空白行
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # 写字典的方法
                writer.writeheader()  # 写表头的方法
        # 接下来追加写入内容
        with open("lianjia.csv", "a", newline='', encoding='utf-8') as csvfile:  # newline='' 一定要写，否则写入数据有空白行
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for house in house_list:
                writer.writerow(house)# 按行写入数据
            print("saving successfully!")
            print("^_^ write success")
        '''
        ############################################################
        with open("lianjia.csv","a", newline='') as f:
            fieldnames = {'区域', '地址', '小区', '租金(元/月)', '租赁方式', '户型', '面积', '朝向', '基本信息', '图片链接', '房源描述'}
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer = csv.writer(f)
            for house in house_list:
                writer.writerow(house)
        print("saving successfully!")

        '''

    def run(self):
        #1.获取url,并生成列表
        url_list = self.get_urllist()
        for url in url_list:
            #2.获取网页响应
            html_str = self.parse(url)
            # 3.解析网页数据
            house_list = self.get_html_content(html_str)
            #4.保存
            self.save_file(house_list)

if __name__ == '__main__':
    lianjiaspyder = LianjiaSpyder()
    lianjiaspyder.run()