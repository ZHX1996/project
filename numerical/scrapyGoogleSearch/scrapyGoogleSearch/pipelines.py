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
import re
import pymysql
import pandas as pd


class ScrapygooglesearchPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeline(object):
    def __init__(self, mysql_host, mysql_port, mysql_user, mysql_password, mysql_db, ngo_file, columns_name):
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_db = mysql_db
        self.ngo_file = ngo_file
        self.columns_name = columns_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'), 
            mysql_port=crawler.settings.get('MYSQL_PORT'),
            mysql_user=crawler.settings.get('MYSQL_USER'), 
            mysql_password=crawler.settings.get('MYSQL_PASSWORD'), 
            mysql_db=crawler.settings.get('MYSQL_DB'),
            ngo_file = crawler.settings.get('NGO_FILE'),
            columns_name = crawler.settings.get('COLUMNS_NAME')
        )

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=self.mysql_host,
            port=self.mysql_port,
            user=self.mysql_user,
            password=self.mysql_password,
            db=self.mysql_db,
            charset='utf8'
        )

        self.cursor = self.connection.cursor()
        self.cursor.execute('show tables;')
        tableNames = [self.cursor.fetchall()] 
        tableNames = str(tableNames) 

        file = pd.read_excel(self.ngo_file,sheet_name='Sheet1', names=self.columns_name)
        df = pd.DataFrame(file)
        df['中文名称'].fillna(df['外文名称'], inplace=True)
        for keyword in df['中文名称'].tolist():
            if tableNames.find(keyword) == -1:
                sql = 'create table `' + keyword + '` (`title` varchar(20) not null, `address` varchar(50), `content` varchar(300), `intro` varchar(50))'
            else:
                sql = 'truncate table `' + keyword + '`'
            self.cursor.execute(sql)
                
    def process_item(self, item, spider):
        if isinstance(item, ScrapygooglesearchItem):
            self.title = item['title'].split('$')
            self.address = item['address'].split('$')

            for i in range(len(self.title)):
                sql = 'insert into `' + item['key'] + '` (title,address) values (' + self.title[i] +',' + self.address[i] + ')'
                self.cursor.execute(sql)

        if isinstance(item, linkBodyItem):
            sql = 'update `' + item['key'] + '` set content=' + item['content'] + ', intro=' + item['intro'] + 'where title=' + item['title'] 
            self.cursor.execute(sql)

        if isinstance(item, facebookIntroItem):
            sql = 'update `' + item['key'] + '` set intro=' + item['intro'] + 'where title=' + item['title'] 
            self.cursor.execute(sql)

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()


class MongodbPipeline(object):
    def __init__(self, mongo_url, mongo_db, max_page, linkKeys, keywords):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
        self.max_page = max_page
        self.linkKeys = linkKeys
        self.keywords = keywords
        self.k = 0
        self.tmp = []
        self.title = []
        self.address = []
        self.a = 0


    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_url=crawler.settings.get('MONGO_URL'), mongo_db=crawler.settings.get('MONGO_DB'),
        linkKeys=crawler.settings.get('WEBSITE_HIGH'), max_page=crawler.settings.get('MAX_PAGE'), keywords=crawler.settings.get('KEYWORDS'))


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url, port=27017)
        self.db = self.client[self.mongo_db]
        collist = self.db.collection_names()
        for key in collist:
            self.db[key].drop()


    def process_item(self, item, spider):
        if isinstance(item, ScrapygooglesearchItem):
            self.title = item['title'].split('$')
            self.address = item['address'].split('$')

            for i in range(len(self.title)):
                self.db[item['key']].insert({self.title[i]: {'address':self.address[i]}})


        if isinstance(item, linkBodyItem):
            cursor = self.db[item['key']].find({item['title']+".address": re.compile(item['address'])})
            for dic in cursor:
                key = [i for i in dic.keys()]
                value = [j for j in dic.values()]
                try:
                    value[1]['content'] = item['content']
                    value[1]['intro'] = item['intro']
                    self.db[item['key']].update_one({key[0]:value[0]}, {'$set':{key[1]:value[1]}}, True)
                except:
                    value[0]['content'] = item['content']
                    value[0]['intro'] = item['intro']
                    self.db[item['key']].update_one({key[1]:value[1]}, {'$set':{key[0]:value[0]}}, True)
            
        

        if isinstance(item, facebookIntroItem):
            cursor = self.db[item['key']].find({item['title']+".address": re.compile(item['address'])})
            for dic in cursor:
                key = [i for i in dic.keys()]
                value = [j for j in dic.values()]
                try:
                    value[1]['intro'] = item['intro']
                    self.db[item['key']].update_one({key[0]:value[0]}, {'$set':{key[1]:value[1]}}, True)
                except:
                    value[0]['intro'] = item['intro']
                    self.db[item['key']].update_one({key[1]:value[1]}, {'$set':{key[0]:value[0]}}, True)
            

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