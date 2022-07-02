import scrapy
import pandas as pd

class Toshiba2Spider(scrapy.Spider):
    name = 'toshiba2'
    # allowed_domains = ['www.store.emprgroup.com.au']
    # start_urls = ['http://www.store.emprgroup.com.au/']

    def start_requests(self):
        df = pd.read_csv('toshiba.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i}, dont_filter=True)

    def parse(self, response):
        # bread1 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[2]/a[1]/text()").get()
        # bread2 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[3]/a[1]/span/text()").get()
        # bread3 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[4]/a[1]/span/text()").get()
        # bread4 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[5]/a[1]/span/text()").get()
        # bread5 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[6]/a[1]/span/text()").get()
        # bread6 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[7]/a[1]/span/text()").get()
        # bread7 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[8]/a[1]/span/text()").get()
        # bread8 = response.xpath("//div[@class='breadcrumbs col-md-12']/ul[1]/li[9]/a[1]/span/text()").get()
        
        # category = response.meta['links']     
        # links = response.xpath("//div[@class='col-lg-4 col-md-4']/a")
        # for link in links:
        #     url = link.xpath(".//@href").get()
        #     text = link.xpath(".//text()").get().strip()
        #     absolute_url = f"https://www.store.emprgroup.com.au{url}"

    #         yield scrapy.Request(url=absolute_url, callback=self.parse_x, meta={'cat':category, 'model':text}, dont_filter=True)
    
    # def parse_x(self, response):
        products = response.xpath("//div[@class='col-lg-12 col-md-12']/div/span/a")
        for product in products:
            prod_link = product.xpath(".//@href").get()
            product_link_full = f"https://store.emprgroup.com.au{prod_link}"
            prod_num = product.xpath(".//text()").get()

            yield{
                'model link':response.request.meta['links'],
                # 'models': text,
                # 'model links':absolute_url
                # 'Breadcrumb1':bread1,
                # 'Breadcrumb2':bread2,
                # 'Breadcrumb3':bread3,
                # 'Breadcrumb4':bread4,
                # 'Breadcrumb5':bread5,
                # 'Breadcrumb6':bread6,
                # 'Breadcrumb7':bread7,
                # 'Breadcrumb8':bread8,
                'part number':prod_num,
                'product link':product_link_full
                }