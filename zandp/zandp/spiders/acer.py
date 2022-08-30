import scrapy
import pandas as pd 

class AcerSpider(scrapy.Spider):
    name = 'acer'
    # allowed_domains = ['www.zandparts.com']
    # start_urls = ['http://www.zandparts.com/']

    def start_requests(self):
        df = pd.read_csv('Book1.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)
    
    def parse(self, response):
        # alternate = response.xpath("//div[@class='product__content']/div/a/span/text()").getall()
        # category = response.xpath("//div[@class='product-detail']/ul/li[4]/text()[2]").get().strip()
        name = response.xpath("//h1[@class='product-detail__name']/text()").get().strip() 
        # part = response.xpath("//div[@class='product-detail']/ul/li/text()[2]").get().strip()
        # desc = response.xpath("//section[@class='tab__content-container']/div[1]/div").get().strip().split("\n")[:3]
        # image = response.xpath("//img[@class='product-detail__image--main']/@src").get()
        # absolute_image = f"https://www.zandparts.com{image}"

        yield{
            'product links':response.meta['links'],
            # 'product category':category,
            'product name':name
            # 'part number':part,
            # 'description':desc,
            # 'image link':absolute_image,
            # 'alt':alternate               
            }
