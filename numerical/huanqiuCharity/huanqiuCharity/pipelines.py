# -*- coding: utf-8 -*-

import csv
from huanqiuCharity.items import HuanqiucharityItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class HuanqiucharityPipeline(object):
    def process_item(self, item, spider):
        return item


class Pipeline_ToCSV(object):  
    def __init__(self):
        store_file = 'C://Users/Administrator.SC-201905252025/Desktop/result.csv'
        self.file = open(store_file,'w', newline='',encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow((
        'sourceUrl',
        'imgsrc',
        'focusArea',
        'ChineseName',
        'EnglishName',
        'focusGroup',
        'introduction',
        'establishedYear',
        'registration',
        'responsible',
        'slogan',
        'email',
        'url',
        'phone',
        'address',
        'donation',
        'sourceofFunds',
        'project',
        'bigThing',
        'award',
        'otherContact'
        ))



    def close_spider(self,spider):
        self.file.close()


    def process_item(self,item,spider):
        self.writer.writerow((
        item['sourceUrl'],
        item['ChineseName'],
        item['EnglishName'],
        item['imgsrc'],
        item['focusArea'],
        item['focusGroup'],
        item['introduction'],
        item['establishedYear'],
        item['registration'],
        item['responsible'],
        item['slogan'],
        item['email'],
        item['url'],
        item['phone'],
        item['address'],
        item['donation'],
        item['sourceofFunds'],
        item['project'],
        item['bigThing'],
        item['award'],
        item['otherContact']
        ))
