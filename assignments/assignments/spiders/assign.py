import scrapy
import pandas as pd

class AssignSpider(scrapy.Spider):
    name = 'assign'
    # allowed_domains = ['www.assingmentspro.com']
    # start_urls = ['http://www.assingmentspro.com/']

    def start_requests(self):
        df = pd.read_csv("C:/Users/Hp/assignment links.csv")
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)
    
    def parse(self, response):
        Title = response.xpath("//h1/a/text()").get().strip()
        Description = response.xpath("//div[@class='entry-content']/div/p/text()").get()

        yield{
            'Links':response.meta['links'],
            'Title':Title,
            'Description':Description
        }
