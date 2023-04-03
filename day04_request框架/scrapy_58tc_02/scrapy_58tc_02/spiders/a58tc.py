import scrapy


class A58tcSpider(scrapy.Spider):
    name = "58tc"
    allowed_domains = ["www.bj.58tc.com"]
    start_urls = ["http://www.bj.58tc.com/"]

    def parse(self, response):
        print('58同城')
