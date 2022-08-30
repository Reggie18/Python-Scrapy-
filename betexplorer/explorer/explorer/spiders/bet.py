import scrapy
import pandas as pd



class BetSpider(scrapy.Spider):
    name = 'bet'
    allowed_domains = ['www.betexplorer.com']
    start_urls = ['https://www.betexplorer.com/soccer/england']

    def parse(self, response):
        league_href = response.xpath("//table[@class='table-main js-tablebanner-t']/tbody/tr/td/a")
        for link in league_href:
            league = link.xpath(".//@href").get()
            absolute_url = f"https://www.betexplorer.com{league}"
            text = link.xpath(".//text()").get()
            total_url = absolute_url + 'results'

            yield scrapy.Request(url=total_url, callback=self.parse_x)

    def parse_x(self, response):
        match_url = response.xpath("//td[@class='h-text-left']/a")
        for url in match_url:
            link = url.xpath(".//@href").get()
            absolute_url = response.urljoin(link)

            link1 = absolute_url + '#1x2'
            link2 = absolute_url + '#ou'
            link3 = absolute_url + '#ah'
            link4 = absolute_url + '#ha'
            link5 = absolute_url + '#dc'
            link6 = absolute_url + '#bts'

            yield{
                'links':absolute_url,
                'link1':link1,
                'link2':link2,
                'link3':link3,
                'link4':link4,
                'link5':link5,
                'link6':link6
            }


    # def start_requests(self):
    #     df = pd.read_csv('Book1.csv')
    #     urlList = df['URL'].to_list()
    #     for i in urlList:
    #         yield scrapy.Request(url = i, callback=self.parse)



    # def parse(self, response):
    #     match_url = response.xpath("//td[@class='h-text-left']/a")
    #     for url in match_url:
    #         link = url.xpath(".//@href").get()
    #         absolute_url = response.urljoin(link)

    #         yield SeleniumRequest(url=absolute_url, callback=self.parse_x, meta={'links':absolute_url}, dont_filter=True)
    
    # def parse_x(self, response):
    #     links = response.meta['links']
    #     event = response.xpath("//ul[@class='list-breadcrumb']/li[5]/span/text()").get()
    #     home = response.xpath("//ul[@class='list-details']/li/h2/a/text()").get()
    #     date_time = response.xpath("//ul[@class='list-details']/li[2]/p[1]/text()").get()
    #     score = response.xpath("//ul[@class='list-details']/li[2]/p[2]/text()").get()
    #     odds = response.xpath("//ul[@class='list-details']/li[2]/h2/text()").get()
    #     away = response.xpath("//ul[@class='list-details']/li[3]/h2/a/text()").get()
    #     home_scorers = response.xpath("//ul[@class='list-details list-details--shooters']/li[1]/table/tbody/tr/td/text()").getall()
    #     away_scorers = response.xpath("//ul[@class='list-details list-details--shooters']/li[2]/table/tbody/tr/td/text()").getall()

    #     yield{
    #         'links':links,
    #         'event':event,
    #         'home team':home,
    #         'away team':away,
    #         'scoreline':score,
    #         'date and time':date_time,
    #         'odds':odds,
    #         'stats home':home_scorers,
    #         'stats away':away_scorers
    #     }

    


