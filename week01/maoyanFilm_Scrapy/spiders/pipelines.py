# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class MaoyanfilmPipeline:
    def process_item(self, item, spider):
        movie = pd.DataFrame(data = [(item['film_title'], item['film_type'], item['plan_date'])])
        movie.to_csv('./movie.csv', mode='a+', encoding='utf_8_sig', index=False, header=False)
        return item
