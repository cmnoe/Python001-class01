import scrapy
from scrapy.selector import Selector
from spiders.items import ShortsItem


class ShortsSpider(scrapy.Spider):
    name = 'shorts'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/1291546/comments?sort=new_score&status=P']

    def parse(self, response):
        shorts = Selector(response=response).xpath("//div[@class='comment']")
        for short in shorts[0:20]:
            item = ShortsItem()
            item['user'] = short.xpath("./h3/span[2]/a/text()").extract()[0]
            class_name = short.xpath("./h3/span[2]/span[contains(@class, 'rating')]/@class").extract()
            item['star'] = int(class_name[0][7:8]) if class_name else 0
            item['content'] = short.xpath("./p/span/text()").extract()[0]
            yield item
