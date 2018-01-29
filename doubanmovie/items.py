# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field as field


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    #id
    id =field()
    #标题
    title = field()
    #链接
    link = field()
    #导演
    directors = field()
    #评分
    rate = field()
    #星级
    star = field()
    #演员
    casts = field()

    image_urls = field()
    images = field()