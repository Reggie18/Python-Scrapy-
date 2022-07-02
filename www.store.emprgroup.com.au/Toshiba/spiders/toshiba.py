# -*- coding: utf-8 -*-
import scrapy
import pandas as pd


class ToshibaSpider(scrapy.Spider):
    name = 'toshiba'
    # allowed_domains = ['www.store.emprgroup.com.au']
    # start_urls = ['http://www.store.emprgroup.com.au/']

    def start_requests(self):
        df = pd.read_csv('toshiba.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)

    def parse(self, response):  
        category = response.meta['links']
        products = response.xpath("//div[@class='col-lg-12 col-md-12']/div/span/a")
        for product in products:
            prod_link = product.xpath(".//@href").get()
            product_link_full = response.urljoin(prod_link)

            yield scrapy.Request(url=product_link_full, callback=self.parse_x, meta={'cat':category,'links':product_link_full}, dont_filter=True)

    def parse_x(self, response):
        

        #breadcrumbs
        
        bread1 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[2]/a[1]/text()").get()
        bread2 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[3]/a[1]/span/text()").get()
        bread3 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[4]/a[1]/span/text()").get()
        bread4 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[5]/a[1]/span/text()").get()
        bread5 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[6]/a[1]/span/text()").get()
        bread6 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[7]/a[1]/span/text()").get()
        # bread7 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[8]/a[1]/span/text()").get()
        # bread8 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[9]/a[1]/span/text()").get()
        
        #get name of product
        product_name = response.xpath("//div[@itemprop='description']/text()").get().strip().replace("\xa0\r\n","")

        #get optional equivalent
        options = response.xpath("//div[@itemprop='description']/b/text()").extract_first()

        #get part number
        part_num = response.xpath("//div[@itemprop='description']//span/strong/text()").extract_first().strip().replace("\r\n","")

        #product html
        product_html = response.xpath("//div[@itemprop='description']").get().strip().split("\n")[:4]

        #get alternatives
        alt = response.xpath("//div[@itemprop='description']/p/text()").extract_first()

        #product image
        image = response.xpath("//a[@itemprop='image']/img/@src").extract_first()

        yield{
                'category link':response.request.meta['cat'],
                'product link':response.request.meta['links'],
                'breadcrumb1':bread1,
                'breadcrumb2':bread2,
                'breadcrumb3':bread3,
                'breadcrumb4':bread4,
                'breadcrumb5':bread5,
                'breadcrumb6':bread6,
                'Product Name':product_name,
                'Part Number':part_num,
                'Description':product_html,
                'Image link':image,
                'Optional Equivalent':options,
                'Alternatives':alt
                # 'part number':prod_num,
                # 'product link':product_link_full
            }

    


    
