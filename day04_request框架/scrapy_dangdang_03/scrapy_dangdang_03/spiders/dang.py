import scrapy
from scrapy_dangdang_03.items import ScrapyDangdang03Item

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    def parse(self, response):
        # pipelines 下载数据
        # item    定义数据结构
        # src = '//ul[@id="component_59"]/li//img/@src'
        # name = '//ul[@id="component_59"]/li//img/@alt'
        # price = '//ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
        # 所有的seletor的对象 都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            # 第一张图片和其他图片的src地址不一样
            src = src or li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            yield ScrapyDangdang03Item(src = src,name = name,price = price)
            print(src,name,price)
        
        # pass
