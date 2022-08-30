# -*- coding: utf-8 -*-
import scrapy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from scrapy_selenium import SeleniumRequest
from shutil import which

class AsusSpider(scrapy.Spider):
    name = 'asus'
    allowed_domains = ['www.zandparts.com']
    # start_urls = ['https://www.zandparts.com/en/gateway']
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_path = which("C:/Users/Hp/Downloads/chromedriver.exe")
    
    #Starting request from just one url
    def start_requests(self):
        yield scrapy.Request('https://www.zandparts.com/en/gateway', self.parse)

    #grabbing the categories and getting all the links to navigate
    def parse(self,response):
        cat_links = response.xpath("//div[@class='category-navigation']/a")
        for link in cat_links:
            category = link.xpath(".//@href").get()
            cat_text = link.xpath(".//h2/text()").get().strip().replace('\r\n','')
            #making the url absolute
            abs = f"https://www.zandparts.com{category}"

            request=scrapy.Request(url=abs, callback=self.parse_x)
            request.cb_kwargs['category']=cat_text
            yield request
    
    #grabbing the series and getting all the links as well
    def parse_x(self, response, **cat_text):
        ser_links = response.xpath("//div[@class='category-navigation']/a")
        for link in ser_links:
            series = link.xpath(".//@href").get()
            ser_text = link.xpath(".//h2/text()").get().strip().replace('\r\n','')
            abs2 = f"https://www.zandparts.com{series}"
            request = scrapy.Request(url=abs2, callback=self.parse_y)
            request.cb_kwargs['series']=ser_text

    #grabbing each model and navigating to the product page for all the data
    def parse_y(self, response, cat_text, **ser_text):
        mod_links = response.xpath("//div[@class='category-navigation']/a")
        for link in mod_links:
            model = link.xpath(".//@href").get()
            mod_text = link.xpath(".//h2/text()").get().strip().replace('\r\n','')
            abs3 = f"https://www.zandparts.com{model}"
            
            request = scrapy.Request(url=abs3, callback=self.parse_z)
            request.cb_kwargs['model'] = mod_text
            yield request

    #product page. Getting the data
    def parse_z(self,response, cat_text, ser_text, **mod_text): 
        products = response.xpath("//div[@class='product__info']/a")
        next_page = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        next_page_full = f"https://www.zandparts.com{next_page}"
        for product in products:
            link = product.xpath(".//@href").get()
            absolute_url = f"https://www.zandparts.com{link}"

          
            request= scrapy.Request(url = absolute_url, callback = self.parse_m)
            request.cb_kwargs['links'] = absolute_url
            yield request
         #navigating through each page to get the data on each page                       
        if next_page:
                yield scrapy.Request(url=next_page_full, callback=self.parse_z)

    def parse_m(self, response, cat_text, ser_text, mod_text, **absolute_url):
        alternate = response.selector.xpath("//div[@class='product__content']/div/a/span/text()").getall()
        category = response.selector.xpath("//div[@class='product-detail']/ul/li[4]/text()[2]").get().strip()
        name = response.selector.xpath("//h1[@class='product-detail__name']/text()").get().strip()
        part = response.selector.xpath("//div[@class='product-detail']/ul/li/text()[2]").get().strip()
        desc = response.selector.xpath("//div[@class='product-detail__description']").get().replace("\r\n","").strip()
        image = response.selector.xpath("//img[@class='product-detail__image--main']/@src").get()
        absolute_image = f"https://www.zandparts.com{image}"
        
        yield{
            'category':cat_text,
            'series':ser_text,
            'model':mod_text,
            'product links':absolute_url,
            'product category':category,
            'product name':name,
            'part number':part,
            'description':desc,
            'image link':absolute_image,
            'alt':alternate               
            }
        
