import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_dushu_04.items import ScrapyDushu04Item


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1188_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1188_\d+\.html"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        # item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        
        img_list = response.xpath('//div[@class="bookslist"]//img')
        for item in img_list:
            name = item.xpath('./@data-original').extract_first()
            src = item.xpath('./@alt').extract_first()
            
            yield ScrapyDushu04Item(name=name,src=src)

