from parse import parse_url
import json

class Douban:
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=1572602942614"

    def get_contentf_list(self,html_str):
        json_dict_str = json.loads(html_str)
        content_list = json_dict_str["subject_collection_items"]
        total = json_dict_str["total"]
        return  content_list,total

    def save_data(self,content_list):
        with open("豆瓣（国产）.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(content["year"])
                f.write("\t")
                f.write("影名：")
                f.write(content["title"])
                f.write("\t")
                f.write("导演：")
                f.write(''.join(str(content["directors"])))#''.join(str(content["directors"]))
                f.write("\t")
                f.write("简评：")
                f.write(content["recommend_comment"])
                f.write("\n")
                print("保存txt文档成功！电影名称："+str(content["title"])+"\n")
        '''
        with open("douban_chinese.json","a",encoding="utf-8") as f:
            for line in content_list:
                print("Saving successfully!")
                f.write(json.dumps(line,ensure_ascii=False))
                f.write("\n")
        with open("豆瓣（国产）.txt","a",encoding="utf-8") as f:
            for content in content_list:
                print("保存txt文档成功！")
                f.write(json.dump(content["title"],ensure_ascii=False))
                f.write("\n")    
        :param content_list:
        :return:
        '''




    def run(self):
        num = 0
        total = 100
        while num<total+18:
            #1.初始化
            url = self.url.format(num)
            #2.获取html响应
            html_str = parse_url(url)
            #3.提取数据
            content_list,total = self.get_contentf_list(html_str)
            #4.保存数据
            self.save_data(content_list)
            num += 18

if __name__ == '__main__':
    douban = Douban()
    douban.run()