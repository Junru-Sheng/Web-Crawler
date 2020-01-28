import requests
from retrying import retry
from lxml import etree
import json
class QidianSpyder:
    def __init__(self):
        self.url = "https://www.qidian.com/rank/hotsales?style=1&page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Referer": "https://www.qidian.com/rank/hotsales?style=1&page=3"
            }
    def get_url_list(self):
        url_list = [self.url.format(i) for i in range(1,6)]
        return url_list

    @retry(stop_max_attempt_number=3)
    def _parse(self,url):
        response = requests.get(url,headers=self.headers,timeout=5)
        return response.content.decode()

    def parse(self,url):
        try:
            html_str = self._parse(url)
        except:
            html_str = None
        return html_str

    def get_content_data(self,html_str):
        html = etree.HTML(html_str)
        book_list = []
        li_list = html.xpath("//div[@class='main-content-wrap fl']/div[@class='rank-body']/div[@id='rank-view-list']/div[@class='book-img-text']/ul/li")
        for li in li_list:
            item = {}

            item["rank"] = li.xpath("./div[@class='book-img-box']/span/text()")
            item["rank"] = item["rank"][0] if len(item["rank"])>0 else None
            print("rank:"+str(item["rank"]))

            item["title"] = li.xpath("./div[@class='book-mid-info']/h4/a/text()")
            item["title"] = item["title"][0] if len(item["title"])>0 else None
            print("title:" + str(item["title"]))

            item["author"] = li.xpath("./div[@class='book-mid-info']/p[@class='author']/a[@class='name']/text()")
            item["author"] = item["author"][0] if len(item["author"])>0 else None

            item["kind"] = li.xpath("./div[@class='book-mid-info']/p[@class='author']/a[@data-eid='qd_C42']/text()")
            item["kind"] = item["kind"][0] if len(item["kind"])>0 else None
            print("kind:"+str(item["kind"]))

            item["intro"] = li.xpath("./div[@class='book-mid-info']/p[@class='intro']/text()")
            item["intro"] = item["intro"][0].strip() if len(item["intro"])>0 else None

            item["update"] = li.xpath("./div[@class='book-mid-info']/p[@class='update']/a/text()")
            item["update"] = item["update"][0] if len(item["update"])>0 else None

            item["book_url"] = li.xpath("./div[@class='book-right-info']/p[@class='btn']/a[@class='red-btn']/@href")
            item["book_url"] = "https:"+item["book_url"][0] if len(item["book_url"])>0 else None
            book_list.append(item)
        return book_list

    def save(self,book_list):
        with open("起点中文小说排行榜.txt",'a',encoding='utf-8') as f:
            for book_dict in book_list:
                f.write(json.dumps(book_dict,ensure_ascii=False))
                f.write('\n')
        print("saving successfully!")

    def run(self):
        # 1.初始化url，获得url列表
        url_list = self.get_url_list()
        for url in url_list:
            #2.发送请求，获取响应
            html_str = self.parse(url)
            #3.获取数据
            book_list = self.get_content_data(html_str)
            #4.保存起来，用txt文本
            self.save(book_list)
if __name__ == '__main__':
    qidian = QidianSpyder()
    qidian.run()






