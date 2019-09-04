# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
import codecs
import csv
from scrapyGoogleSearch.items import ScrapygooglesearchItem, linkBodyItem, facebookIntroItem


class ScrapygooglesearchPipeline(object):
    def process_item(self, item, spider):
        return item


class MongodbPipeline(object):
    def __init__(self, mongo_url, mongo_db, max_page, linkKeys):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
        self.max_page = max_page
        self.linkKeys = linkKeys
        self.k = 0
        self.tmp = []
        self.title = []
        self.address = []
        self.a = 0


    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_url=crawler.settings.get('MONGO_URL'), mongo_db=crawler.settings.get('MONGO_DB'),
        linkKeys=crawler.settings.get('WEBSITE_HIGH'), max_page=crawler.settings.get('MAX_PAGE'))


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url, port=27017)
        self.db = self.client[self.mongo_db]
        collist = self.db.collection_names()
        if 'high' in collist:
            self.db.high.drop()
        if 'low' in collist:
            self.db.low.drop()


    def process_item(self, item, spider):
        if isinstance(item, ScrapygooglesearchItem):
            self.a += 1
            self.title += item['title'].split(';')
            self.address += item['address'].split(';')
            if self.a == self.max_page:
                for i in range(len(self.title)):
                    if i == 0:
                        self.db.high.update({'address': self.address[i]},{"$set":{'address': self.address[i], 'title': self.title[i]}}, True)
                        self.tmp.append(self.address[i])
                    else:
                        self.k = 0
                        for j in range(len(self.tmp)):
                            if self.tmp[j] in self.address[i] or self.address[i] in self.tmp[j]:
                                self.k += 1
                        if self.k == 0:
                            self.tmp.append(self.address[i])

                            for linkKey in self.linkKeys:
                                if linkKey in self.address[i]:
                                    self.k += 1
                            if self.k > 0:
                                self.db.high.update({'address': self.address[i]},{"$set":{'address': self.address[i], 'title': self.title[i]}}, True)
                            else:  
                                self.db.low.update({'address': self.address[i]},{"$set":{'address': self.address[i], 'title': self.title[i]}}, True)
                self.title,self.address,self.a,self.tmp = [],[],0,[]

        if isinstance(item, linkBodyItem):
            self.k = 0
            for linkKey in self.linkKeys:
                if linkKey in item['address']:
                    self.k += 1
            if self.k > 0:
                self.db.high.update({'address': item['address']},{"$set":{'content': item['content'], 'intro':item['intro']}}, False)
            else:  
                self.db.low.update({'address': item['address']},{"$set":{ 'content': item['content'], 'intro':item['intro']}}, False)
        

        if isinstance(item, facebookIntroItem):
            self.db.high.update({'address':item['address']}, {"$set":{'intro':item['intro']}}, False)

    def close_spider(self, spider):
        self.client.close()



class Pipeline_ToCSV(object):
 
    def __init__(self, linkKeys, max_page):
        self.max_page = max_page
        self.linkKeys = linkKeys
        self.k = 0
        self.tmp = []
        self.title = []
        self.address = []
        self.a = 0
        store_file_high = 'C:/Users/Administrator.SC-201905252025/Desktop/result_high.csv'
        self.file_high = open(store_file_high,'w', newline='',encoding='utf-8')
        self.writer_high = csv.writer(self.file_high)
        store_file_low = 'C:/Users/Administrator.SC-201905252025/Desktop/result_low.csv'
        self.file_low = open(store_file_low,'w', newline='',encoding='utf-8')
        self.writer_low = csv.writer(self.file_low)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(linkKeys=crawler.settings.get('WEBSITE_HIGH'), max_page=crawler.settings.get('MAX_PAGE'))
        
    def process_item(self,item,spider):
        self.a += 1
        self.title += item['title'].split(';')
        self.address += item['address'].split(';')
        if self.a == self.max_page:
            for i in range(len(self.title)):
                if i == 0:
                    self.writer_high.writerow((self.title[i],self.address[i]))
                    self.tmp.append(self.address[i])
                else:
                    self.k = 0
                    for j in range(len(self.tmp)):
                        if self.tmp[j] in self.address[i] or self.address[i] in self.tmp[j]:
                            self.k += 1
                    if self.k == 0:
                        self.tmp.append(self.address[i])

                        for linkKey in self.linkKeys:
                            if linkKey in self.address[i]:
                                self.k += 1
                        if self.k > 0:
                            self.writer_high.writerow((self.title[i],self.address[i]))
                        else:  
                            self.writer_low.writerow((self.title[i],self.address[i]))
            self.title,self.address,self.a,self.tmp = [],[],0,[]
            
    
    def close_spider(self,spider):
        self.file_high.close()
        self.file_low.close()