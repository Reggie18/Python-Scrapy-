from selenium import webdriver
import scrapy
from scrapy.selector import Selector
import time


class Timken3Spider(scrapy.Spider):
    name = 'timken3'
    allowed_domains = ['www.timken-us.ptplace.com']
    start_urls = ['https://timken-us.ptplace.com/productSearch?categoryId=5502799']

    def __init__(self):
        scrapy.Spider.__init__(self)
        options1 = webdriver.ChromeOptions()
        options1.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.br = webdriver.Chrome("C:/Users/Hp/Downloads/chromedriver.exe", options=options1)

    def parse(self, response):
        pages = range(1216)
        for _ in pages:
            hxs = Selector(response)
            self.br.get(response.url)
            links = hxs.xpath("//a[@class='no-link-in-print']")
            for link in links:
                full_link = f"www.timken-us.ptplace.com{link.xpath('.//@href').get()}"

                yield{
                    'links':full_link
                }
            if next_page := self.br.find_element_by_xpath("//div[@class='btn-flex']/div/bdo[@data-label='next']"):
                next_page.click()
