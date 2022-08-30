from scrapy import signals


class SaveErrorsMiddleware(object):
    def __init__(self, crawler):
        crawler.signals.connect(self.close_spider, signals.spider_closed)
        crawler.signals.connect(self.open_spider, signals.spider_opened)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def open_spider(self, spider):
        self.output_file = open('error links.txt', 'a')

    def close_spider(self, spider):
        self.output_file.close()

    def process_spider_exception(self, response, exception, spider):
        self.output_file.write(response.url + '\n')