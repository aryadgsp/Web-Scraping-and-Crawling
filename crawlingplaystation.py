# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class h1_tagsSpider(CrawlSpider):
    name = 'h1_tags'
    allowed_domains = ['store.playstation.com']
    start_urls = ['https://store.playstation.com/en-id']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        all_headings = response.xpath('//h1/text()').getall()
        
        for heading in all_headings:
            yield {
                'text': heading,
                'page': response.url
            }
