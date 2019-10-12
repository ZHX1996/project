# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ScrapygooglesearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    collection = 'info'
    key = Field()
    title = Field()
    address = Field()

class linkBodyItem(scrapy.Item):
    collection = 'bodyContent'
    key = Field()
    content = Field()
    title = Field()
    intro = Field()
    address = Field()

class facebookIntroItem(scrapy.Item):
    title = Field()
    address = Field()
    key = Field()
    intro = Field()