import scrapy
import pandas as pd

class YachtSpider(scrapy.Spider):
    name = 'yacht'
    #allowed_domains = ['www.superyachttimes.com']
    #start_urls = ['https://www.superyachttimes.com/companies']

    def start_requests(self):
        df = pd.read_csv('Book1.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse, meta={'links':i})

    def parse(self,response):
        next_page = response.xpath("//span[@class='next']/a/@href").get()
        next_page_full = f"https://www.superyachttimes.com{next_page}"
        service_name = response.xpath("//div[@class='selected-filter-value']/div/text()[2]").get().strip()
        # services = response.xpath("//div[@class='tags']/div/text()").getall()
        containers = response.xpath("//article")
        for container in containers:
            names = container.xpath(".//div[@class='textual']/div/div/div[@class='h1 title company_title']/text()").get().strip()
        # image = response.xpath("//img[@class='profile-photo']/@src").get()
        # images = f'{image}.jpg'

        # containers = response.xpath("//article")
        # for container in containers:
        #     image_urls = container.xpath(".//div/div/@style").get()
        #     name = container.xpath(".//div[@class='textual']/div/div/a/text()").get()
        # name = response.xpath("//div[@class='h1 title company_title']/text()").extract_first().strip()
        # # names = str(name).strip().replace("\n","")
        # country = response.xpath("//div[@class='country']/text()").get()
        # address1 = response.xpath("//section[@class='labeled-section info']/div[1]/text()").getall()
        # ad1 = str(address1).replace(","," ").replace("\n","").replace("'","")
        # website = response.xpath("//section[@class='labeled-section info']/p/a/@href").get()
        # address2 = response.xpath("//section[@class='labeled-section info']/div[2]/text()").get()
        # # ad2 = str(address2).replace(","," ").replace("\n","")
        # phone = response.xpath("//section[@class='labeled-section info']//div[@class='phone']/text()").get()
        # # email = response.xpath("//section[@class='labeled-section info']//div[@class='email']/a/text()").get()

            yield{  
                'Services':service_name,
                # 'Image Links':image_urls
                'Name':names
                    # 'Country':country,
                    # 'address 1':ad1,
                    # 'address 2':address2,
                    # 'Phone':phone,
                    # 'website':website,
                }

        if next_page:
            yield scrapy.Request(url=next_page_full, callback=self.parse)


