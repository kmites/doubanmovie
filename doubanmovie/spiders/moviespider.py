# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DoubanmovieItem

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0']

    base_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start='
    offset = 0

    def parse(self, response):

        #返回数据为json格式,转换为python dict
        movie_info = json.loads(response.text)
        #获取返回数据
        data = movie_info["data"]
        #判断返回数据是否为空
        if len(data) == 0:
            return

        #提取数据
        for info in data:
            item = DoubanmovieItem()

            item["id"] = info["id"]
            item["title"] = info["title"]
            item["link"] = info["url"]
            item["directors"] = info["directors"]
            item["rate"] = info["rate"]
            item["star"] = int(info["star"])/10
            item["casts"] =info["casts"]
            item["image_urls"] = [info["cover"]]
            yield item
        self.offset +=20
        yield scrapy.Request(self.base_url+str(self.offset),callback=self.parse)


