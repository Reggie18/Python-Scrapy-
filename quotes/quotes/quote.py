
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        container = response.xpath("//div[@class='col-md-8']/div")
        for item in container:
            quote = item.xpath(".//span[1]/text()").get()
            name = item.xpath(".//span[2]/small/text()").get()
            author_link = item.xpath(".//span[2]/a/@href").get()
            full_link = response.urljoin(author_link)

            yield{
                'Quote':quote,
                'Author':name,
                'About Link':full_link
            }

process = CrawlerProcess(get_project_settings())
process.crawl(QuoteSpider)
process.start()
