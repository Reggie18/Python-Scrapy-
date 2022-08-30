# -*- coding: utf-8 -*-
import scrapy


class AppleSpider(scrapy.Spider):
    name = 'apple'
    allowed_domains = ['www.thebookyard.com']
    start_urls = ['http://www.thebookyard.com/']

    def parse(self, response):
        pass
