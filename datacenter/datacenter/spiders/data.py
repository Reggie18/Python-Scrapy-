import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    # allowed_domains = ['datacentersupport.lenovo.com/gb/en']
    # start_urls = ['http://datacentersupport.lenovo.com/gb/en/']

    def parse(self, response):
        bread1 = response.xpath("//span[@class='prod-catagory-name']/text()").get().replace("\xa0\xa0>\xa0\xa0","")
        bread2 = response.xpath("//span[@class='prod-catagory-name']/a/text()").get()
        rows = response.xpath("//table/tbody")
        for row in rows:
            part_num = row.xpath(".//tr/td[2]/div/text").get()

            pagination = response.xpath("//div[@class='page-container']/span[5]")