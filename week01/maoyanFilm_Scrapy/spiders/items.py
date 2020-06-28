# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanfilmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    film_title = scrapy.Field()
    film_type = scrapy.Field()
    plan_date = scrapy.Field()

