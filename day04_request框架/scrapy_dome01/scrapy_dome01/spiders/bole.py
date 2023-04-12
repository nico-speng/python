import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_dome01.items import ScrapyDome01Item


class BoleSpider(CrawlSpider):
    name = "bole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ["http://blog.jobbole.com/touzi/yy/index.html"]

    rules = (Rule(LinkExtractor(allow=r"/yy/index_\d+\.html"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        
        data_list = response.xpath('//div[@class="article-list"]//div[@class="list-item"]')
        
        for item in data_list:
            src = item.xpath('.//img/@src').extract_first()
            title = item.xpath('.//h1/text()').extract_first()
            content = item.xpath('./div[@class="content"]//div[2]/text()').extract_first()
            times = item.xpath('.//div[@class="about-left"]/span[1]/text()').extract_first()
            tag = item.xpath('.//div[@class="about-left"]/span[2]/text()').extract_first()    

            yield ScrapyDome01Item(src = src,title = title,content = content,times = times,tag = tag)
