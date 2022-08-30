import scrapy
import pandas as pd

class DatenSpider(scrapy.Spider):
    name = 'daten'
    # allowed_domains = ['www.vbi.de/planerdatenbank/a-hagl-gmbh-5571/']
    # start_urls = ['http://www.vbi.de/planerdatenbank/a-hagl-gmbh-5571//']

    def start_requests(self):
        df = pd.read_csv('daten.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)
    
    def parse(self, response):
        name = response.xpath("//div[@class='misc w-100 d-flex flex-column']/span/text()").get()
        address = response.xpath("//div[@class=' col-12 col-md-4 address d-flex flex-column mb-4 mb-md-0']/span/text()").get()
        zip_code =response.xpath("//div[@class=' col-12 col-md-4 address d-flex flex-column mb-4 mb-md-0']/span[2]/text()").get().split(" ")[0]
        city = response.xpath("//div[@class=' col-12 col-md-4 address d-flex flex-column mb-4 mb-md-0']/span[2]/text()").get().split(" ")[1]
        industry = response.xpath("//div[@class='firstLetter']/text()").get()

        yield{
            'links':response.meta['links'],
            'Names':name,
            'Address':address,
            'zip':zip_code,
            'city':city,
            'Industry':industry
        }