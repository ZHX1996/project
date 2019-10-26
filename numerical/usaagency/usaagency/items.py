# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class UsaagencyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    firstCategory = Field()
    secondCategory = Field()
    thirdCategory = Field()
    chineseName = Field()
    englishName = Field()
    firstLink = Field()
    linkAddress = Field()
    parentAgency = Field()
    # about = Field()
    contact = Field()
    contactZh = Field()
    intro = Field()
    introZh = Field()

class aboutItem(scrapy.Item):
    chineseName = Field()
    about = Field()
    aboutZh = Field()
