import scrapy

'''
1、引擎向spiders要url
2、引擎将要爬取的url给调度器
3、调度器会将url生成请求对象放入到指定的队列中4、从队列中出队一个请求
5、引擎将请求交给下载子进行处理
6、下载器发送请求获取互联网数据
7、下载器将数据返回给引擎
8、引擎将数据再次给到spiders
9、 spiders通过xpath解析该数据，得到数据或url10、spiders将数据或者url给到引擎
11、引擎判断该数据还是url，是数据，交给管道( itempipeline )处理，是url交给调度器处理


'''

class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["https://car.autohome.com.cn/price/brand-15.html"]
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        # 获取宝马系列名称和价格
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')
        
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name,price)
         
