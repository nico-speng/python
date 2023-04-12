# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
import csv

import urllib.request

class ScrapyDome01Pipeline:
    
    def __init__(self):
        # CSV文件路径
        self.csv_file = 'scrapy_data.csv'

        # 判断CSV文件是否存在，如果不存在则创建新文件
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as fp:
                writer = csv.writer(fp)
                # 写入CSV文件的表头
                writer.writerow(['标题','内容', '图片地址','浏览数','发布时间'])
                
    
    def process_item(self, item, spider):
        
        # 将数据写入CSV文件中
        with open(self.csv_file, 'a', newline='', encoding='utf-8') as fp:
            writer = csv.writer(fp)
            writer.writerow([item['title'], item['content'],item['src'],item['tag'],item['times']])

        return item
    
# 多条管道开启
# 一、定义管道类
# 二、在setting开启管道
class DangDownloadPipeline:
    def process_item(self,item,spider):
        
        url = item.get('src')

        if url is not None:
            folder = './img/'
            if not os.path.exists(folder):
                os.makedirs(folder)
            filename = os.path.join(folder, item.get('title') + '.jpg')
            urllib.request.urlretrieve(url=url, filename=filename)

        return item
