import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class RealtorSpider(scrapy.Spider):
    name = 'realtor'
    # allowed_domains = ['www.realtor.com']
    # start_urls = ['https://www.realtor.com/realestateagents/houston_tx/photo-1/pg-5']

    def start_requests(self):
        df = pd.read_csv('Book1.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse)

    def parse(self, response):
        # next_page = response.xpath("//a[@aria-label='Go to next page']/@href").get()
        # next_page_full = f"https://www.realtor.com/realestateagents/houston_tx/photo-1/{next_page}"
        cards = response.xpath("//ul[@class='jsx-372421607']/div")
        for card in cards:
            links = card.xpath(".//div/div//div[@class='jsx-3970352998 agent-list-card-title-text clearfix']/a/@href").get()
            name = card.xpath(".//div/div//div[@class='jsx-3970352998 agent-list-card-title-text clearfix']/a/div/text()").get()
            card_links = f"https://www.realtor.com{links}"

            yield SeleniumRequest(
                    url=card_links,
                    callback=self.parse_x,
                    wait_time=5,
                    wait_until=EC.presence_of_element_located((By.XPATH, "//div[@class='jsx-4242887589 better-homes-and-gar-icon-right']")),
                    meta={'links':card_links, 'names':name},
                    dont_filter=True
                )
            # yield scrapy.Request(url=card_links, callback=self.parse_x, meta={'links':card_links})
            # if next_page:
            #     yield scrapy.Request(url=next_page_full, callback=self.parse)


    def parse_x(self, response):
        company_name = response.xpath("//div[@class='jsx-4242887589 better-homes-and-gar-icon-right']/p/text()").get()
        address = response.xpath("//div[@class='jsx-4242887589 better-homes-and-gar-icon-right']/p[@class='jsx-4242887589 agent_address']/span/text()").getall()
        cor_address = str(address).replace(",","|").replace("'","").replace("[","").replace("]","")

        yield{
            'link':response.meta['links'],
            'Name':response.meta['names'],
            'Company Name':company_name,
            'Address':cor_address
        }
