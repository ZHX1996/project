# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
import json
import codecs
import csv
from scrapyGoogleSearch.items import ScrapygooglesearchItem, linkBodyItem, facebookIntroItem, officialIntroItem
import re
# import pymysql
import pandas as pd
# import sqlite3


class ScrapygooglesearchPipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLPipeline(object):
    def __init__(self):
        summarize = './summarize.csv'
        self.file_summarize = open(summarize,'w', newline='',encoding='utf-8')
        self.writer_summarize = csv.writer(self.file_summarize)

        linkBody = './linkBody.csv'
        self.file_linkBody = open(linkBody,'w', newline='',encoding='utf-8')
        self.writer_linkBody = csv.writer(self.file_linkBody)

        facebookIntro = './facebookIntro.csv'
        self.file_facebookIntro = open(facebookIntro,'w', newline='',encoding='utf-8')
        self.writer_facebookIntro = csv.writer(self.file_facebookIntro)

    #    officialIntro = './officialIntro.csv'
    #   self.file_officialIntro = open(officialIntro,'w', newline='',encoding='utf-8')
    #  self.writer_officialIntro = csv.writer(self.file_officialIntro)


                
    def process_item(self, item, spider):
        if isinstance(item, ScrapygooglesearchItem):
            self.title = item['title'].split('$$')
            self.address = item['address'].split('$$')

            for i in range(len(self.title)):
                self.writer_summarize.writerow((self.title[i], item['key'], self.address[i]))


        if isinstance(item, linkBodyItem):
            self.writer_linkBody.writerow((item['title'], item['category'], item['content'], item['intro']))

        if isinstance(item, facebookIntroItem):
            self.writer_facebookIntro.writerow((item['title'], item['intro']))

    #    if isinstance(item, officialIntroItem):
    #        self.writer_officialIntro.writerow((item['title'], item['intro'], item['category']))


    def close_spider(self, spider):
        self.file_facebookIntro.close()
        self.file_linkBody.close()
        #self.file_officialIntro.close()
        self.file_summarize.close()
