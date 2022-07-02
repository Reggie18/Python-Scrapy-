# -*- coding: utf-8 -*-
import scrapy
import pandas as pd


class PartsSpider(scrapy.Spider):
    name = 'parts'
    # allowed_domains = ['www.parts-people.com']
    # start_urls = ['http://www.parts-people.com/']

    def start_requests(self):
        df = pd.read_csv('Book1.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse)

    def parse(self, response):
        brand = response.xpath("//span[@class='headline']/@text()").extract()
        group = response.xpath("//div[@class='small-4 columns']/strong/@text()").extract()


        rows = response.xpath("(//*[@id='top-wrapper']/div[1]/div/table)[2]/tbody/tr")
        for row in rows:
            models = row.xpath(".//td[1]/a/text()").extract()
            model_link = row.xpath(".//td[1]/a/href").extract()
            arts = row.xpath(".//td[2]/a/text()").extract()
            description = row.xpath(".//td[3]/a/text()").extract()
    

            yield {
                'brand':brand,
                'group':group,
                'model':models,
                'model links':model_link,
                'article':arts,
                'Description':description,
            }
