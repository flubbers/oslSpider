# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from tutorial.items import DmozItem
from tutorial.pipelines import FicheroJsonTagsPipeline,FicheroJsonPipeline
class DmozSpider(BaseSpider):
    name = "osl"
    allowed_domains = ["osl.ugr.es"]
    start_urls = [
        "http://osl.ugr.es/",
        "http://osl.ugr.es/page/2/",
        "http://osl.ugr.es/page/3/",
    ]

    def parse(self, response):
    	hxs = HtmlXPathSelector(response)
        ficheroTags = FicheroJsonTagsPipeline()
        ficheroNoTags = FicheroJsonPipeline()

        noticia = DmozItem()

        nodo = hxs.select('//div[@class="entry hentry"]')
        for xs in nodo:
            noticia['title'] = xs.select('.//h2[@class="entry-title"]/a/text()').extract()
            noticia['content'] = xs.select('.//div[@class="entry-content"]/p/text()').extract()
            noticia['cat'] = xs.select('.//span[@class="entry-categories"]/a/text()').extract()
            noticia['tag'] = xs.select('.//span[@class="entry-tags"]/a/text()').extract()
            if noticia['tag']:
                ficheroTags.process_item(noticia,self)
            else:
                ficheroNoTags.process_item(noticia,self)
