#!/usr/bin/python

import scrapy

class ItapoSpider(scrapy.Spider):
    name = "Itapo"
    allowed_domains = ["itaponews.com.br"]
    start_urls = [
        "http://www.itaponews.com.br/category/noticias/itaporanga/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, "wb") as f:
            f.write(response.body)


