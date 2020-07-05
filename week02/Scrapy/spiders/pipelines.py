# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
from spiders.mysql import ConnDB

sql = """CREATE TABLE FILMS (
    film_title CHAR(255) NOT NULL,
    film_type CHAR(255),
    plan_date CHAR(255)
)ENGINE=innodb DEFAULT CHARSET=utf8;"""

class MaoyanfilmPipeline:
    def __init__(self):
        self.db = ConnDB()

    def process_item(self, item, spider):
        # self.film_list.append([(item['film_title'], item['film_type'], item['plan_date'])])
        self.db.insert((item['film_title'], item['film_type'], item['plan_date']))
        return item

    def open_spider(self, spider):
        self.db.run(sql)
    
    def close_spider(self, spider):
        self.db.close()

