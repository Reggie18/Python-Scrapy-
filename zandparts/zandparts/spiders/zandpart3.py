# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from shutil import which

class Zandpart3Spider(scrapy.Spider):
    name = 'zandpart3'
    # allowed_domains = ['https://www.zandparts.com/sv/asus-14g154026100']
    # start_urls = ['https://www.zandparts.com/']

    def __init__(self):
        df = pd.read_csv('zandpart.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_path = which("C:/Users/Hp/Downloads/chromedriver.exe")
            self.start_urls = [i]
            driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
            driver.get(i)
            popup = driver.find_element_by_xpath("//button[@id]")
            popup.click()
            try:
                alt_item = driver.find_element_by_xpath("//nav[@class='tab__header-container']/label[3]")
                alt_item.click()
                self.html = driver.page_source
                driver.close()
            except NoSuchElementException:
                self.html = driver.page_source
                driver.close()
                
    def parse(self,response):
        response = Selector(text=self.html)
        crumbs = response.xpath("//ul[@class='breadcrumbs']/text()").get()
        name = response.xpath("//h1[@class='product-detail__name']/text()").get().strip()
        part = response.xpath("//div[@class='product-detail']/ul/li/text()").get().strip()
        desc = response.xpath("//div[@class='product-detail__description']").get().replace('\n',' ')
        image = response.xpath("//img[@class='product-detail__image--main']/@src").get().strip()
        alternatives = response.xpath("//div[@class='product__content']/div/a/span")
        for alt in alternatives:
            alternative = alt.xpath(".//text()").getall()

            yield{
                'crumbs':crumbs,
                'name':name,
                'part number':part,
                'description':desc,
                'image link':image,
                'alternatives':alternative
            }
