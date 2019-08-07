# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
import codecs
import csv


class ScrapygooglesearchPipeline(object):
    def process_item(self, item, spider):
        return item


class MongodbPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db


    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_url=crawler.settings.get('MONGO_URL'), mongo_db=crawler.settings.get('MONGO_DB'))


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url, port=27017)
        self.db = self.client[self.mongo_db]
        collist = self.db.collection_names()
        if 'titleLink' in collist:
            self.db.titleLink.drop()


    def process_item(self, item, spider):
        self.db.titleLink.insert(dict(item))
        return item

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