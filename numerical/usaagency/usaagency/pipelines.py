# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from usaagency.items import UsaagencyItem, aboutItem


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
            sql = 'create table `agency` (`chineseName` varchar(50) not null, `englishName` varchar(50), `parentAgency` varchar(20),  `firstCategory` varchar(20), `secondCategory` varchar(20), `thirdCategory` varchar(20), `intro` varchar(400), `introZh` varchar(80), `firstLink` varchar(100), `linkAddress` varchar(200), `contact` varchar(150), `contactZh` varchar(150), `about` varchar(9000), `aboutZh` varchar(3000))'
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
            sql = 'update `agency` set about=%s, aboutZh=%s where chineseName=%s'
            self.cursor.execute(sql, (item['about'], item['aboutZh'], item['chineseName']))
            self.connection.commit()


    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
