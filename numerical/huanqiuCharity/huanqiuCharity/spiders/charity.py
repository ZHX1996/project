# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy import Request, Spider
from huanqiuCharity.items import HuanqiucharityItem

class CharitySpider(scrapy.Spider):
    name = 'charity'
    allowed_domains = ['charity.huanqiu.com']
    start_urls = ['http://charity.huanqiu.com/hope/ngo']


    def parse(self, response):
        links = response.xpath('//*[@id="rst-content"]//a/@href').extract()
        links = ['http://charity.huanqiu.com' + link for link in links]

        num = response.xpath('//*[@id="item-count"]/span/text()').extract()[0]
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.0.1594 Safari/537.36',
        'Host': 'charity.huanqiu.com',
        'Origin': 'http://charity.huanqiu.com',
        'Referer': 'http://charity.huanqiu.com/hope/ngo',
        'Connection': 'keep-alive'
        }

        def constructDatas(offset):
            return {'limit': '6', 'offset': offset}

        for offset in range(15, int(num), 6):
            r = requests.post('http://charity.huanqiu.com/hope/Appajax', headers = header, data=constructDatas(offset))
            resJson = r.json()
            for tmp in resJson['data']:
                tmp = dict(tmp)
                links.append(tmp['eName'])

        for link in links:
            yield Request(url = link, callback=self.parse_linkBody, dont_filter=True)
        


    def parse_linkBody(self, response):
        charityItem = HuanqiucharityItem()
        charityItem['sourceUrl'] = response.url

        imgsrc = response.xpath('/html/body/div[4]/div[1]/div[1]/img/@src').extract()
        focusArea = response.xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/text()').extract()
        ChineseName = response.xpath('/html/body/div[4]/div[1]/div[1]/h2/text()').extract()
        EnglishName = response.xpath('/html/body/div[4]/div[1]/div[1]/span/text()').extract()
        focusGroup = response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/div[2]/text()').extract()
        introduction = response.xpath('/html/body/div[4]/div[1]/div[1]/div[3]/text()').extract()
        establishedYear = response.xpath('//*[@id="base-info"]/dl[1]/dd/text()').extract()
        registration = response.xpath('//*[@id="base-info"]/dl[2]/dd/text()').extract()
        responsible = response.xpath('//*[@id="base-info"]/dl[3]/dd/text()').extract()
        slogan = response.xpath('//*[@id="slogan"]//p//text()').extract()
        email = response.xpath('//*[@id="contact"]/dl[1]/dd/text()').extract()
        url = response.xpath('//*[@id="contact"]/dl[2]/dd/a/@href').extract()
        phone = response.xpath('//*[@id="contact"]/dl[3]/dd/text()').extract()
        address = response.xpath('//*[@id="contact"]/dl[4]/dd/text()').extract()

        def litostr(li):
            return ''.join([i.strip() for i in li])

        imgsrc = litostr(imgsrc)
        focusArea = litostr(focusArea)
        ChineseName = litostr(ChineseName)
        EnglishName = litostr(EnglishName)
        focusGroup = litostr(focusGroup)
        introduction = litostr(introduction)
        establishedYear = litostr(establishedYear)
        registration = litostr(registration)
        responsible = litostr(responsible)
        slogan = litostr(slogan)
        email = litostr(email)
        url = litostr(url)
        phone = litostr(phone)
        address = litostr(address)

        # 资金来源 大事记 所获奖项  其他联系方式
        # 捐款方式 项目信息   有大小标题
        dic = {'资金来源': 'sourceofFunds',
        '大事记':'bigThing',
        '所获奖项':'award',
        '其他联系方式':'otherContact',
        '捐款方式':'donation',
        '项目信息':'project'}
        tmp = response.xpath('/html/body/div[4]/div[2]/div').extract()
        for i in range(2, len(tmp)+1):
            k = response.xpath('/html/body/div[4]/div[2]/div['+str(i)+']//text()').extract()            
            k = list(filter(None, [l.strip() for l in k ]))
            # m = ''
            # if k[0] == '项目信息':
            #     try:
            #         for i in range(1, len(k), 2):
            #             m += k[i]+':'+k[i+1]
            #     except:
            #         m = ' '.join(k[1:])
            # else:
            #     m = ' '.join(k[1:])
            
            # charityItem[dic[k[0]]] = m
            charityItem[dic[k[0]]] = '$'.join(k[1:])
        
        for k in list(dic.values()):
            try:
                charityItem[k] 
            except:
                charityItem[k] = ' '

        
        charityItem['imgsrc'] = imgsrc
        charityItem['focusArea'] = focusArea
        charityItem['ChineseName'] = ChineseName
        charityItem['EnglishName'] = EnglishName
        charityItem['focusGroup'] = focusGroup
        charityItem['introduction'] = introduction
        charityItem['establishedYear'] = establishedYear
        charityItem['registration'] = registration
        charityItem['responsible'] = responsible
        charityItem['slogan'] = slogan
        charityItem['email'] = email
        charityItem['url'] = url
        charityItem['phone'] = phone
        charityItem['address'] = address

        yield charityItem


    def start_requests(self):
        url = self.start_urls[0]
        yield Request(url=url, callback=self.parse, dont_filter=True)