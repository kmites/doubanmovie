# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class DoubanmoviePipeline(object):

    def open_spider(self,spider):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.doubanmovie

    def process_item(self, item, spider):
        self.db.movieinfo.insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()