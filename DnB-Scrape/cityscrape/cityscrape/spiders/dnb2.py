import scrapy
import pandas as pd
from scrapy_selenium import SeleniumRequest

class Dnb2Spider(scrapy.Spider):
    name = 'dnb2'
    # allowed_domains = ['www.dnb.com']
    # start_urls = ['http://www.dnb.com/']

    def start_requests(self):
            df = pd.read_csv("C:/Users/Hp/Desktop/git training/dnb links koln.csv")
            urlList = df['Links2'].to_list()
            for i in urlList:
                yield SeleniumRequest(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)

    def parse(self,response):
        name = response.xpath("//div[@class='col-md-6 company-profile-overview-starting-margin']/div/span/span/text()").get()
        website = response.xpath("//div[@id='company_profile_snapshot']/div[4]/div[@class='col-md-11']/span/span/a/@href").get()
        phone = response.xpath("//div[@id='company_profile_snapshot']/div[3]/div[@class='col-md-11']/span/span/text()").get()
        Address = response.xpath("//div[@id='company_profile_snapshot']/div[2]/div[@class='col-md-11']/span/span/text()").get()

        yield{
            'company Name':name,
            'Website':website,
            'Phone Number':phone,
            'Address':Address
        }