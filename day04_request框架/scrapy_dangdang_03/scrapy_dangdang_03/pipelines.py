# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果要使用管道就需要在setting.py 中开启管道
class ScrapyDangdang03Pipeline:
    # 在爬虫文件开始之前就执行的一个方法
    def open_spider(self,spider):
        self.fp = open('book.json','w',encoding='utf-8')
        
    # itme 就是yield后面的book对象
    def process_item(self, item, spider):
        
        self.fp.write(str(item))
        
        # 以下模式不推荐 因为没传递过来一个对象 就打开一次文件 对文件的操作过去频繁
        # write方法必须是要写一个字符串，而不能是其他的对象
        # with open('book.json','a+',encoding='utf-8') as fp:
        #     fp.write(str(item))
        return item
    
    def close_spider(self,spider):
        self.fp.close()
        
    import urllib.request

    # 多条管道开启
    class DangDownloadPipeline:
        def process_item(self,item,spider):
            
            urllib.request.url
            
            return item
