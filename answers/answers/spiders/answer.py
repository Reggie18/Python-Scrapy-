import scrapy
import pandas as pd

class AnswerSpider(scrapy.Spider):
    name = 'answer'
    # allowed_domains = ['www.radioactivetutors.com']
    # start_urls = ['https://www.radioactivetutors.com/ExpertAnswers/']

    def start_requests(self):
        df = pd.read_csv("C:/Users/Hp/Documents/radioactive.csv")
        urlList = df['URL'].to_list()
        for i in urlList:
            yield scrapy.Request(url = i, callback=self.parse_x, meta={'links':i}, dont_filter=True)
    
    # def parse(self, response):
    #     links = response.xpath("//div[@class='row justify-content-center']/div/div/div/div/div/h3/a")
    #     next_page = response.xpath("//div[@class=' m-2 text-center ']/a/@href").get()
    #     for link in links:
    #         urls = link.xpath(".//@href").get()

    #         yield scrapy.Request(url=urls, callback=self.parse_x, meta={'links':urls})

    #         if next_page:
    #             yield scrapy.Request(url=next_page, callback=self.parse)

    
    def parse_x(self,response):
        header = response.xpath("//h1/text()").get().strip()
        content = response.xpath("//div[@class='col-md-9']/div[2]/div[1]/div/p/text()").get().strip()

        yield{
            'links':response.meta['links'],
            'Title':header,
            'Description':content
        }


