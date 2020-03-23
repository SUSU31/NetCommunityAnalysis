# -*- coding: utf-8 -*-
import scrapy
import json
from hothubspider.items import HothubspiderItem


class hothubSpider(scrapy.spiders.Spider):
    name = "spd"
    allowed_domains = ["tophub.today"]
    start_urls = [
        "https://tophub.today/n/KqndgxeLl9"
    ]

    def parse(self, response):
        for i in response.xpath('//tbody/tr'):
            item = HothubspiderItem()
            item['ids'] = i.xpath('td[1]/text()').extract_first()
            item['text'] = i.xpath('td[2]/a/text()').extract_first()
            item['index'] = i.xpath('td[3]/text()').extract_first()
            item['url'] = i.xpath('td[2]/a/@href').extract_first()
            yield item
        
