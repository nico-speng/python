# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ScrapyDushu04Pipeline:
    
    # 在爬虫文件开始之前就执行的一个方法
    def open_spider(self,spider):
        self.fp = open('book.json','w',encoding='utf-8')
    
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self,spider):
        self.fp.close()
   
# 加载setting文件   
from scrapy.utils.project import get_project_settings    
import pymysql

class MysqlPipeline:
    
    def open_spider(self,spider):
        setting = get_project_settings()
        
        self.host = setting['DB_HOST']
        self.port = setting['DB_PORT']
        self.user = setting['DB_USER']
        self.password = setting['DB_PASSWROD']
        self.name = setting['DB_NAME']
        self.charset = setting['DB_CHARSET']
        
        self.connect()
        
    def connect(self):
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.name,
            charset = self.charset,
        )
        
        self.cursor = self.conn.cursor()
    
    def process_item(self, item, spider):
        sql = f"""insert into book(name,src) values("{item['name']}","{item['src']}")"""
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()
        
        return item
    
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()