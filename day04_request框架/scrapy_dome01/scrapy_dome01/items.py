# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDome01Item(scrapy.Item):
    # define the fields for your item here like:
    src = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    times = scrapy.Field()
    tag = scrapy.Field()
