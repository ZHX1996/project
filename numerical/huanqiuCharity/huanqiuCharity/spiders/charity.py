# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy import Request, Spider
from huanqiuCharity.items import HuanqiucharityItem
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

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

        # links = ['http://charity.huanqiu.com/crisis_control_ministry',
        #          'http://charity.huanqiu.com/actspwc',
        #          'http://charity.huanqiu.com/jewish_world_watch']


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
        slogan = response.xpath('//*[@id="slogan"]//p//text()').extract()

        def litostr(li):
            return ''.join([i.strip() for i in li])

        imgsrc = litostr(imgsrc)
        focusArea = litostr(focusArea)
        ChineseName = litostr(ChineseName)
        EnglishName = litostr(EnglishName)
        focusGroup = litostr(focusGroup)
        introduction = litostr(introduction)
        slogan = litostr(slogan)


        charityItem['imgsrc'] = imgsrc
        charityItem['focusArea'] = focusArea
        charityItem['ChineseName'] = ChineseName
        charityItem['EnglishName'] = EnglishName
        charityItem['focusGroup'] = focusGroup
        charityItem['introduction'] = introduction
        charityItem['slogan'] = slogan

        dic = {'资金来源': 'sourceofFunds',
        '大事记':'bigThing',
        '所获奖项':'award',
        '其他联系方式':'otherContact',
        '捐款方式':'donation',
        '项目信息':'project',
        '缩写名称：': 'abbreviation',
        '成立年份：': 'establishedYear',
        '负责人：': 'responsible',
        '注册地：': 'registration',
        '邮箱：': 'email',
        '网址：': 'url',
        '电话：': 'phone',
        '地址：': 'address',
        '本地名称：': 'localName',
        '图片链接': 'imgsrc',
        '源链接': 'sourceUrl',
        '关注领域': 'focusArea',
        '中文名称': 'ChineseName',
        '英文名称': 'EnglishName',
        '关注群体': 'focusGroup',
        '简介': 'introduction',
        '口号': 'slogan'
        }

        tmp = response.xpath('/html/body/div[4]/div[2]/div').extract()
        for i in range(2, len(tmp)+1):
            k = response.xpath('/html/body/div[4]/div[2]/div['+str(i)+']//text()').extract()            
            k = list(filter(None, [l.strip().replace('\n', '') for l in k ]))
            charityItem[dic[k[0]]] = '$'.join(k[1:])

        tmp = response.xpath('//*[@id="base-info"]//text()').extract()
        for i in range(1, len(tmp), 2):
            try:
                charityItem[dic[tmp[i]]] = tmp[i+1]
            except:
                charityItem[dic[tmp[i]]] = 'null'
                print("awsl")

        tmp = response.xpath('//*[@id="contact"]//text()').extract()
        for i in range(1, len(tmp), 2):
            charityItem[dic[tmp[i]]] = tmp[i+1]


        for k in list(dic.values()):
            try:
                charityItem[k]
            except:
                charityItem[k] = 'null'

        yield charityItem


    def start_requests(self):
        url = self.start_urls[0]
        yield Request(url=url, callback=self.parse, dont_filter=True, errback=self.print_err)
        

    def print_err(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('awsl HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('awsl DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('awsl TimeoutError on %s', request.url)
        else:
            request = failure.request
            self.logger.error('awsl on %s', request.url)