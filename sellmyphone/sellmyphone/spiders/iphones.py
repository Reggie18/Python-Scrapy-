from urllib.parse import urljoin
import scrapy
from scrapy_splash import SplashRequest

class IphonesSpider(scrapy.Spider):
    name = 'iphones'
    allowed_domains = ['sellmymobile.com']
    start_urls = ['https://sellmymobile.com/phones/apple']

    def parse(self, response):
        containers = response.xpath("//ul[@class='devices-to-results']/li")
        for item in containers:
            names = item.xpath(".//div//div[@class='device-to-results__name']/text()").get()
            variants = item.xpath(".//div/div/ul/li/a/@href").getall()
            for link in variants:
                full_link = f"https://www.sellmymobile.com{link}"

                yield{
                    'Names':names,
                    'links':full_link
                }
