import scrapy
import pandas as pd

class VcardsSpider(scrapy.Spider):
    name = 'vcards'
    # allowed_domains = ['www.sothebysrealty.com']
    # start_urls = ['http://www.sothebysrealty.com/']

    def start_requests(self):
        df = pd.read_csv('Book1.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i})

    def parse(self, response):
        vcards = response.xpath("//div[@class='GetInTouch__add']/a/@href").get()

        yield{
            'Links':response.meta['links'],
            'Vcard Links':vcards
        }

        
