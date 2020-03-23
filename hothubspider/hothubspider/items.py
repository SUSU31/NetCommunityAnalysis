# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HothubspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ids = scrapy.Field()
    text = scrapy.Field()
    index = scrapy.Field()
    url = scrapy.Field()
