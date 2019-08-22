# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HuanqiucharityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sourceUrl = scrapy.Field()
    imgsrc = scrapy.Field()
    focusArea = scrapy.Field()
    ChineseName = scrapy.Field()
    EnglishName = scrapy.Field()
    focusGroup = scrapy.Field()
    introduction = scrapy.Field()
    establishedYear = scrapy.Field()
    registration = scrapy.Field()
    responsible = scrapy.Field()
    slogan = scrapy.Field()
    email = scrapy.Field()
    url = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    sourceofFunds = scrapy.Field()
    project = scrapy.Field()
    bigThing = scrapy.Field()
    award = scrapy.Field()
    otherContact = scrapy.Field()
    donation = scrapy.Field()
