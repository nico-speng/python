import scrapy
from scrapy_dangdang_03.items import ScrapyDangdang03Item

class DangSpider(scrapy.Spider):
    name = "dang"
    #如果是多页下载的话那么必须要调整的是allowed_domains的范围  一般情况下只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]
    # http://category.dangdang.com/cp01.01.02.00.00.00.html
    # http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
    
    str_url = 'http://category.dangdang.com/cp01.01.02.00.00.00.html'
    page = 1
    
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
            # 获取一个book就将book交给pipelines下载
            yield ScrapyDangdang03Item(src = src,name = name,price = price)
            # print(src,name,price)
        
        if self.page < 20:
            self.page += 1
            url = self.str_url.replace('cp', f'pg{self.page}-cp') if self.page > 1 else self.str_url
            print(f'这是循环网址：{url}')
            
            # 怎么去调用parse方法
            # scrapy . Request就是scrpay的get请求url就是请求地址
            # callback是你要执行的那个函数注意不需要加()
            yield scrapy.Request(url=url,callback=self.parse)
        