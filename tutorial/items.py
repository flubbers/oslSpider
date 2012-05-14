# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class DmozItem(Item):
    title = Field()
    content = Field()
    cat = Field()
    tag = Field()