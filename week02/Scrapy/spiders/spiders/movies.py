# -*- coding: utf-8 -*-
import scrapy
from spiders.items import MaoyanfilmItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    
    # 解析函数
    def parse(self, response):
        films = Selector(response=response).xpath("//div[@class='movie-hover-info']")
        for film in films[0:10]:
            item = MaoyanfilmItem()
            item['film_title'] = film.xpath("./div[1]/@title").extract_first().strip()
            item['film_type'] = film.xpath("./div[2]/text()").extract()[1].strip()
            item['plan_date'] = film.xpath("./div[4]/text()").extract()[1].strip()
            yield item

