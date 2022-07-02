# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy_splash import SplashRequest


class RollerSpider(scrapy.Spider):
    name = 'roller'
    # allowed_domains = ['www.precisionroller.com']
    # start_urls = ['http://www.precisionroller.com/']

    def start_requests(self):
        df = pd.read_csv('Book1.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)

    def parse(self, response):
        # category =response.meta['links']
        # product_links = response.xpath("//table[@class='product-table']/tbody/tr/td[2]/a[1]")
        # for link in product_links:
        #     links = link.xpath(".//@href").get()

        #     yield{
        #         'Category Links':category,
        #         'Product Links':links
        #     }
            # yield scrapy.Request(url=links, callback=self.parse_x, meta={'product links':links, 'category':category}, dont_filter=True)
    
    # def parse_x(self,response):

        brand = response.xpath("//td[@class='body']/div/div[3]/a/text()").get()
        model = response.xpath("//td[@class='body']/div/div[4]/a/text()").get()
        category = response.xpath("//td[@class='body']/div/div[5]/a/text()").get()

        name = response.xpath("//h1/text()").get().strip()
        image_link = response.xpath("//td[@valign='top']/a/img/@src").get()
        absolute_img = f"https://www.precisionroller.com{image_link}"
        Mfr_PN = response.xpath("//div[@id='specs']/ul[1]/li[7]").get().strip().split("\n")[:3]
        Condition = response.xpath("//div[@id='specs']/ul[1]/li[3]").get().split("\n")[3].strip()
        yield{
                'product link':response.request.meta['links'],
                'brand':brand,
                'model':model,
                'part category':category,
                'product name':name,
                'image':absolute_img,
                'Part Number':Mfr_PN,
                'Condition':Condition
            }
