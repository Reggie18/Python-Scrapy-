import scrapy
import pandas as pd

class PanditSpider(scrapy.Spider):
    name = 'pandit'
    # allowed_domains = ['www.essaypandit.com']
    # start_urls = ['http://www.essaypandit.com/']

    def start_requests(self):
        df = pd.read_csv("C:/Users/Hp/pandit links.csv")
        urlList = df['links'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)

    def parse(self, response):
        title = response.xpath("//h1/text()").get().strip()
        category = response.xpath("//div[@class='vcex-post-content-blocks wpex-content-w wpex-clr']/ul/li[@class='meta-category']/a/text()").get()
        content = response.xpath("//div[@class='vcex-post-content-blocks wpex-content-w wpex-clr']/div/ol/li/text()").extract()
        contents = str(content).replace(","," ")
        yield{
            'links':response.meta['links'],
            'post_content':contents,
            'post_title':title,
            'post_category':category
        }
