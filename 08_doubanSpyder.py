import requests
import json
from parse import parse_url
class DoubanSpyder:

    def __init__(self):#初始化
        self.init_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=1572419433583"

    def get_contentf_list(self,html_str):
        data = json.loads(html_str)
        content_list = data["subject_collection_items"]
        print(content_list)
        total = data["total"]
        return content_list,total

    def save_json(self,content_list):
        with open("豆瓣影评(英美).json","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print("Saving Successfully!")


    def run(self):#实现主要逻辑
        #1.start_url
        num=0
        total=100
        while num<total+18:
            url=self.init_url.format(num)
            #2.发送请求,获取响应
            html_str = parse_url(url)
            #3.提取数据
            content_list,total = self.get_contentf_list(html_str)
            #4.保存
            self.save_json(content_list)
            #5.下一页，继续执行2-5步骤
            num += 18
if __name__ == '__main__':
    douban = DoubanSpyder()
    douban.run()