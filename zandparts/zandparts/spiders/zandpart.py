# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import pandas as pd


class ZandpartSpider(scrapy.Spider):
    name = 'zandpart'
    allowed_domains = ['www.zandparts.com']
    # start_urls = ['http://www.zandparts.com/']
    script = '''

                 function main(splash, args)
                    url = args.url
                    assert(splash:go(url))
                    assert(splash:wait(5))
                    alternatives = assert(splash:select("label[for=product-available-alternatives]"))
                    alternatives:mouse_click()
                    assert(splash:wait(2))
                    return {
                        image = splash:png(),
                        html = splash:html()
                    }
                 end  

            '''
    def start_requests(self):
        # df = pd.read_csv('zandpart.csv')
        # urlList = df['URL'].to_list()
        # for i in urlList:
        yield SplashRequest(url="https://www.zandparts.com/sv/asus-14g154026100", callback=self.parse, endpoint='execute', args={
            'lua_source':self.script
        })

    def parse(self,response):
        print(response.body)
        
