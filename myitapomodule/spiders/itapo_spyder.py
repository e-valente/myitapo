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

        title = response.xpath('//title/text()').extract()

        tmptitlelist = response.xpath('//ul/li/a/@href').extract()
        tmpdesclist = response.xpath('//ul/li/a/text()').extract()


        print title

        for i in range(3):
            link = tmptitlelist[i]
            desc = tmpdesclist[i]
            print(("%s -> %s") % (desc, link))





        '''
        with open(filename, "wb") as f:
            f.write(response.body)

        '''


