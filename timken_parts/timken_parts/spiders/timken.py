import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy_splash import SplashRequest
import pandas as pd

class TimkenSpider(scrapy.Spider):
    name = 'timken'
    # allowed_domains = ['www.timken-us.ptplace.com']
    # start_urls = ['http://www.timken-us.ptplace.com/']
    

    # script = '''
    #     function main(splash, args)
    #         assert(splash:go(args.url))
    #         assert(splash:wait(10))
    #         return splash:html()
    #     end
    # '''

    def start_requests(self):
        # df = pd.read_csv('Book1.csv')
        # urlList = df['URL'].to_list()
        # for i in urlList:
        #     yield SplashRequest(url=i, callback=self.parse, endpoint='execute', args={
        #             'lua_source':self.script
        #         }, meta={'links':i})
        df = pd.read_csv('Book1.csv')
        urlList = df['URL'].to_list()
        for i in urlList:
            yield SeleniumRequest(url = i, callback=self.parse, meta={'links':i})

    def parse(self, response):
        bread = response.xpath("//ol[@class='breadcrumb pb-0 mb-0 px-0 pt-3 pt-md-0']//text()").extract()
        breadcrumbs = str(bread).replace("'","").replace("[","").replace("]","").replace(",","|")
        name = response.xpath("//section[@class='mx-4 css-1qtw8py eusrh160']/div[3]/bdo/b/text()").get()
        image = response.xpath("//div[@class='thumbnail-image zoomable-in ml-auto mr-5 e13oy1ej0 css-9gacqy e8j0mv00']/label/img/@src").get()
        assembly_breakdown = response.xpath("//ul[@class='mb-0 fa-ul']/li[2]/a/@href").get()
        assem_link = f"http://www.timken-us.ptplace.com{assembly_breakdown}"
        draw_image = response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[1]/td[2]/bdo/img/@src").get()
        draw_image_link = f"http://www.timken-us.ptplace.com{draw_image}"
        table_row_11= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[1]/td[1]//bdo/text()").get()
        table_row_12= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[1]/td[2]//bdo/text()").get()
        table_row_21= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[2]/td[1]//bdo/text()").get()
        table_row_22= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[2]/td[2]//bdo/text()").get()
        table_row_31= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[3]/td[1]//bdo/text()").get()
        table_row_32= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[3]/td[2]//bdo/text()").get()
        table_row_41= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[4]/td[1]//bdo/text()").get()
        table_row_42= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[4]/td[2]//bdo/text()").get()
        table_row_51= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[5]/td[1]//bdo/text()").get()
        table_row_52= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[5]/td[2]//bdo/text()").get()
        table_row_61= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[6]/td[1]//bdo/text()").get()
        table_row_62= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[6]/td[2]//bdo/text()").get()
        table_row_71= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[7]/td[1]//bdo/text()").get()
        table_row_72= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[7]/td[2]//bdo/text()").get()
        table_row_81= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[8]/td[1]//bdo/text()").get()
        table_row_82= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[8]/td[2]//bdo/text()").get()
        table_row_91= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[9]/td[1]//bdo/text()").get()
        table_row_92= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[9]/td[2]//bdo/text()").get()
        table_row_101= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[10]/td[1]//bdo/text()").get()
        table_row_102= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[10]/td[2]//bdo/text()").get()
        table_row_111= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[11]/td[1]//bdo/text()").get()
        table_row_112= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[11]/td[2]//bdo/text()").get()
        table_row_121= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[12]/td[1]//bdo/text()").get()
        table_row_122= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[12]/td[2]//bdo/text()").get()
        table_row_131= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[13]/td[1]//bdo/text()").get()
        table_row_132= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[13]/td[2]//bdo/text()").get()
        table_row_141= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[14]/td[1]//bdo/text()").get()
        table_row_142= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[14]/td[2]//bdo/text()").get()
        table_row_151= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[15]/td[1]//bdo/text()").get()
        table_row_152= response.xpath("//table[@class='table table-striped w-auto mb-3']/tbody/tr[15]/td[2]//bdo/text()").get()
        # weight = response.xpath("//div[@class='font-weight-bolder h1 ']/div/bdo[@class='weight small align-self-end css-epvm6 ewjiqvs0']/text()").get()
        code = response.xpath("//div[@class='w-100 pb-2 mb-2 border-dashed border-gray-dark border-bottom-only'][2]/span/text()").get()



        yield{
            'Link':response.meta['links'],
            'UPC Code':code,
            'Breadcrumbs':breadcrumbs,
            'Part Name':name,
            'Image Link':image,
            'Assembly Breakdown Link':assem_link,
            'Drawing Link':draw_image_link,
            'table_data 1':table_row_11,
            'table_data 2':table_row_12,
            'table_data 3':table_row_21,
            'table_data 4':table_row_22,
            'table_data 5':table_row_31,
            'table_data 6':table_row_32,
            'table_data 7':table_row_41,
            'table_data 8':table_row_42,
            'table_data 9':table_row_51,
            'table_data 10':table_row_52,
            'table_data 11':table_row_61,
            'table_data 12':table_row_62,
            'table_data 13':table_row_71,
            'table_data 14':table_row_72,
            'table_data 15':table_row_81,
            'table_data 16':table_row_82,
            'table_data 17':table_row_91,
            'table_data 18':table_row_92,
            'table_data 19':table_row_101,
            'table_data 20':table_row_102,
            'table_data 21':table_row_111,
            'table_data 22':table_row_112,
            'table_data 23':table_row_121,
            'table_data 24':table_row_122,
            'table_data 25':table_row_131,
            'table_data 26':table_row_132,
            'table_data 27':table_row_141,
            'table_data 28':table_row_142,
            'table_data 29':table_row_151,
            'table_data 30':table_row_152
        }
        
