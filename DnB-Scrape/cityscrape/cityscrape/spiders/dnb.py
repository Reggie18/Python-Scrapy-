import scrapy
from scrapy_selenium import SeleniumRequest

class DnbSpider(scrapy.Spider):
    name = 'dnb'
    allowed_domains = ['www.dnb.com']
    start_urls = ['https://www.dnb.com/business-directory/company-information.retail_trade.de.nordrhein-westfalen.duisburg.html?page=1']

    def start_requests(self):
        url = 'https://www.dnb.com/business-directory/company-information.retail_trade.de.nordrhein-westfalen.duisburg.html?page=1'
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self,response):
        companies = response.xpath("//div[@id='companyResults']/div[@class='col-md-12 data']/div/a")
        next_page = response.xpath("//ul[@id='pagination']/li[@class='next']/a/@href").get()
        for company in companies:
            name = company.xpath(".//text()").get()
            link = company.xpath(".//@href").get()

    #         yield scrapy.Request(url=link, callback=self.parse_x, meta={'name':name})
    #     if next_page:
    #         yield SeleniumRequest(url=next_page, callback=self.parse)
    
    # def parse_x(self,response):
    #     Name = response.meta['name']
    #     website = response.xpath("//div[@id='company_profile_snapshot']/div[4]/div[@class='col-md-11']/span/span/a/@href").get()
    #     phone = response.xpath("//div[@id='company_profile_snapshot']/div[3]/div[@class='col-md-11']/span/span/text()").get()
    #     Address = response.xpath("//div[@id='company_profile_snapshot']/div[2]/div[@class='col-md-11']/span/span/text()").get()

        yield{
            'company Name':name,
            'Website':link
            # 'Phone Number':phone,
            # 'Address':Address
        }


