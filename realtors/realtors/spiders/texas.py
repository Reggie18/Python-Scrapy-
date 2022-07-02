import scrapy


class TexasSpider(scrapy.Spider):
    name = 'texas'
    allowed_domains = ['www.texasrealestate.com']
    start_urls = ['https://www.texasrealestate.com/realtors/realtor-search-results/?sid=865226023984&location=&state=TX&first_name=&last_name=&firm_name=&license_number=&representation=&language=&results_page=1383']

    def parse(self, response):
        next_page = response.xpath("//li[@class='is-pulled-right '][1]/a/@href").get()
        next_page_full = f"https://www.texasrealestate.com/realtors/realtor-search-results/{next_page}"
        realtor_details = response.xpath("//article[@class='realtor-details']")
        for detail in realtor_details:
            realtor_name = detail.xpath(".//div[@class='realtor-info']/h5/a/text()").get()
            realtor_address1 = detail.xpath(".//div[@class='realtor-info']/div[@class='realtor-address']/div[1]/text()").get()
            realtor_address2 = detail.xpath(".//div[@class='realtor-info']/div[@class='realtor-address']/div[2]/text()").get()
            realtor_address3 = detail.xpath(".//div[@class='realtor-info']/div[@class='realtor-address']/div[3]/text()").get()

            yield{
                'Name':realtor_name,
                'Address 1':realtor_address1,
                'Address 2':realtor_address2,
                'Address 3':realtor_address3
            }
        if next_page:
            yield scrapy.Request(url=next_page_full, callback=self.parse)

