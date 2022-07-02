from operator import pos
import scrapy


class SkilledSpider(scrapy.Spider):
    name = 'skilled'
    allowed_domains = ['skilledpapers.com']
    start_urls = ['https://skilledpapers.com/author/linus/']

    def parse(self, response):
        articles = response.xpath("//article")
        for article in articles:
            title = article.xpath(".//header/h2/a/text()").get()
            link = article.xpath(".//header/h2/a/@href").get()
            content = article.xpath(".//div[@class='entry-content']//text()").getall()
            category = article.xpath(".//footer/span/a/text()").get()

            yield {
                'post_title':title,
                'post_content':content,
                'post_category':category,
                'post_link':link
            }
        if next_page := response.xpath(
            "//div[@class='nav-links']/div[@class='nav-previous']/a/@href"
        ).get():
            yield scrapy.Request(url=next_page, callback=self.parse)
