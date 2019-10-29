# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from usaagency.items import UsaagencyItem, aboutItem
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagePipeline(ImagesPipeline):
    default_headers = {
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
    }

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    
    def item_completed(self, results, item, info):
        if isinstance(item, aboutItem):
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                item['logo'] = item['logo_url']
                # raise DropItem('failed')
        return item


    def get_media_requests(self, item, info):
        if isinstance(item, aboutItem):
            if item['logo_url'] != "" and item['logo_url'] != None:
                self.default_headers['referer'] = item['logo_url']
                yield Request(item['logo_url'], headers=self.default_headers)
        


class UsaagencyPipeline(object):
    def __init__(self, mysql_host, mysql_port, mysql_user, mysql_password, mysql_db):
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_db = mysql_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'), 
            mysql_port=crawler.settings.get('MYSQL_PORT'),
            mysql_user=crawler.settings.get('MYSQL_USER'), 
            mysql_password=crawler.settings.get('MYSQL_PASSWORD'), 
            mysql_db=crawler.settings.get('MYSQL_DB')
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

        if tableNames.find('agency') == -1:
            sql = 'create table `agency` (`chineseName` varchar(50) not null, `englishName` varchar(100), `parentAgency` varchar(100),  `firstCategory` varchar(20), `secondCategory` varchar(20), `thirdCategory` varchar(20), `intro` varchar(400), `introZh` varchar(80), `firstLink` varchar(100), `linkAddress` varchar(200), `contact` varchar(150), `contactZh` varchar(150), `about` varchar(9000), `aboutZh` varchar(3000), `logo` varchar(200))'
        else:
            sql = 'truncate table `agency`'
        self.cursor.execute(sql)
        self.connection.commit()
                
    def process_item(self, item, spider):
        if isinstance(item, UsaagencyItem):
            sql = 'insert into `agency` (chineseName, englishName, parentAgency, firstCategory, secondCategory, thirdCategory, intro, introZh, firstLink, linkAddress, contact, contactZh) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (item['chineseName'],item['englishName'],item['parentAgency'],item['firstCategory'],item['secondCategory'],item['thirdCategory'],item['intro'],item['introZh'],item['firstLink'],item['linkAddress'],item['contact'],item['contactZh']))
            self.connection.commit()

        if isinstance(item, aboutItem):
            sql = 'update `agency` set about=%s, aboutZh=%s, logo=%s where linkAddress=%s'
            self.cursor.execute(sql, (item['about'], item['aboutZh'], item['logo'], item['linkAddress']))
            self.connection.commit()
        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
