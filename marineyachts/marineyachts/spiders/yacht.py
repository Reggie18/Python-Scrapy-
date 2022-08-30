from scrapy_splash import SplashRequest
import scrapy
import pandas as pd

class YachtSpider(scrapy.Spider):
    name = 'yacht'
    # allowed_domains = ['www.marinetraffic.com']
    # start_urls = ['http://www.marinetraffic.com/']

    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(15))
            return splash:html()
        end
    '''
    def start_requests(self):
        # df = pd.read_csv('Book1.csv')
        # urlList = df['URL'].to_list()
        # for site in urlList:
        yield SplashRequest(url='https://www.marinetraffic.com/en/global-search/?term=azzam', callback=self.parse, endpoint='execute', args={
                'lua_source':self.script
            })


    def parse(self,response):
        container = response.xpath("//div[@class='MuiGrid-root jss155 MuiGrid-item']/div")
        for item in container:
            link = item.xpath(".//a/@href").get()
            first_name = item.xpath(".//a//div[@class='jss211']/div/h5//span[@class]/text()").get()
            other_names = item.xpath(".//a//div[@class='jss211']/div/h5/text()").get()
            Details = item.xpath(".//a//div[@class='jss212']/span/text()").get()

            yield{
                # 'links':response.meta['links'],
                'yacht links':link,
                'first name':first_name,
                'Others':other_names,
                'Details':Details
            }
            



