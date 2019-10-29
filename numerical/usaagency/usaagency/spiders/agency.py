# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy import Request, Spider
from urllib.parse import quote
import re
import json
import html
import time
import pandas as pd
import logging
from usaagency.items import UsaagencyItem, aboutItem
from googletrans import Translator
import os
from urllib.parse import urljoin


class AgencySpider(scrapy.Spider):
    name = 'agency'
    allowed_domains = ['www.usa.gov']
    start_urls = ['https://www.usa.gov/']
    trans = Translator()


    def parse(self, response, firstCategory, secondCategory, thirdCategory, chineseName, englishName):
        item_1 = UsaagencyItem()
        item_1['firstCategory'] = firstCategory
        item_1['secondCategory'] = secondCategory
        item_1['thirdCategory'] = thirdCategory
        item_1['chineseName'] = chineseName
        item_1['englishName'] = englishName
        item_1['firstLink'] = response.url
        item_1['linkAddress'],item_1['contact'],item_1['contactZh'],item_1['intro'],item_1['introZh'] = "","","","",""
        address, number, tollfree = [],[],[]
        
        item_1['intro'] = "".join(response.xpath('//*[@id="content"]/div/div/article/header[1]/p//text()').extract())
        item_1['introZh'] = self.trans.translate(item_1['intro'], dest='zh-CN').text

        sections = response.xpath("//*[@id='content']/div/div/article//section")
        for section in sections:
            if "Website" in "".join(section.xpath('header/h3/text()').extract()):
                item_1['linkAddress'] = section.xpath('p/a/@href').extract()[0]
            if "Main Address" in "".join(section.xpath('header/h3/text()').extract()):
                address = section.xpath('p//text()').extract()
            if "Phone Number" in "".join(section.xpath('header/h3/text()').extract()):
                number = section.xpath('p//text()').extract()
            if "Toll Free" in "".join(section.xpath('header/h3/text()').extract()):
                tollfree = section.xpath('p//text()').extract()
            if "Parent Agency" in "".join(section.xpath('header/h2/text()').extract()):
                item_1['parentAgency'] = self.process_contact(section.xpath('ul//li//a//text()').extract())
        number = number + tollfree
        item_1['contact'] = "address:" + self.process_contact(address) + "; phone number:" + self.process_contact(number)
        item_1['contactZh'] = self.trans.translate(item_1['contact'], dest='zh-CN').text
        yield item_1

        
        tmp = "about " + englishName
        url = "https://www.google.com/search?q=" + "+".join(tmp.split(' '))
        yield Request(url=url, callback = lambda response, linkAddress=item_1['linkAddress']: self.parse_link(response, linkAddress), dont_filter=True)
        

    def parse_link(self, response, linkAddress):
        links = response.xpath('//div[@class="rc"]/div[@class="r"]//a//@href').extract()
        links.sort(key = lambda i:len(i),reverse=False) 
        for link in links:
            if "about" in link:
                # print("\n\n")
                yield Request(url=link, callback=lambda response, linkAddress=linkAddress: self.parse_about(response, linkAddress), dont_filter=True)
                break


    def parse_about(self, response, linkAddress):
        item_2 = aboutItem()

        item_2['logo'] = ""
        item_2['logo_url'] = ""
        item_2['linkAddress'] = linkAddress
        about = self.process_about(response.text)
        item_2['about'] = about
        item_2['aboutZh'] = self.trans.translate(about, dest='zh-CN').text
        root_path = os.path.abspath(self.settings.get('IMAGES_STORE'))

        img_list = response.xpath("//div//img//@src").extract()[::-1]
        for i in range(len(img_list)):
            if 'logo' in img_list[i] or 'symbol' in img_list[i]:
                if 'http' not in img_list[i]:
                    # tmp = linkAddress[:-1] + img_list[i]
                    tmp = urljoin(linkAddress, img_list[i])
                else:
                    tmp = img_list[i]
                if 'https' not in tmp:
                    tmp = re.sub(r'http', 'https', tmp)
                item_2['logo_url'] = tmp
                item_2['logo'] = os.path.join(root_path, img_list[i].split('/')[-1])
                break
        yield item_2


    def process_contact(self, info):
        info = list(map(lambda x: x.strip(), info))
        return " ".join(info)


    def process_about(self, tmp):
        # tmp = re.sub(r'\n', '', tmp)
        tmp = re.sub(r'\r', '', tmp)
        tmp = re.sub(r'\t', '', tmp)
        tmp = re.sub(r'"', "'", tmp)
        tmp = html.unescape(tmp)
        # tmp = re.sub(r'gb2312', 'utf-8', tmp)

        pattern = re.compile(r'<script.*?</script>', re.DOTALL)
        tmp = pattern.sub(r'', tmp)
        pattern = re.compile(r'<scip.*?</scip>', re.DOTALL)
        tmp = pattern.sub(r'', tmp)
        pattern = re.compile(r'<style.*?</style>', re.DOTALL)
        tmp = pattern.sub(r'', tmp)
        # pattern = re.compile(r'<.*?</[\w\W]*?>', re.DOTALL)
        # tmp = pattern.sub(r'', tmp)
        pattern = re.compile(r'<[\w\W]*?>')
        tmp = pattern.sub(r'', tmp)

        # 去除4字节字符
        try:
            pattern = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            pattern = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        tmp = pattern.sub(u'',tmp)

        tmp = re.sub(r'\n+', '\n', tmp)
        tmp = " ".join(tmp.split())
        return tmp


    def start_requests(self):
        logger = logging.getLogger(__name__)
        logger.error("the log level is error")
        # logger.warn("the log level is warning")

        file = pd.read_excel(self.settings.get('FILE_NAME'),sheet_name='Sheet1', names=self.settings.get('COLUMNS_NAME') )
        df = pd.DataFrame(file)
        for i in range(len(df)):
            url = df.iloc[i]['一级链接']
            firstCategory = df.iloc[i]['一级类别']
            secondCategory = df.iloc[i]['二级类别']
            thirdCategory = df.iloc[i]['三级类别']
            chineseName = df.iloc[i]['中文名称']
            englishName = df.iloc[i]['英文名称']
            yield Request(url=url, callback=lambda response, firstCategory=firstCategory, secondCategory=secondCategory, thirdCategory=thirdCategory, chineseName=chineseName, englishName=englishName:self.parse(response, firstCategory, secondCategory, thirdCategory, chineseName, englishName), dont_filter=True)
