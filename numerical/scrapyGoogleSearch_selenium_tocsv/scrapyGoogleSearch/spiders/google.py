# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyGoogleSearch.items import ScrapygooglesearchItem, linkBodyItem, facebookIntroItem
from scrapy.shell import inspect_response
import re
import json
import html


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['www.google.com']
    start_urls = 'https://www.google.com/search?q='


    def parse(self, response):
        # inspect_response(response, self)

        products = response.xpath('//div[@id="rso"]/div/div[contains(@class,"srg")]/div[contains(@class,"g")]')
        for product in products:
            address = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/@href').extract()
            title = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/h3/div/text()').extract()
            break

        item = ScrapygooglesearchItem()
        item['title'] = ';'.join(title)
        item['address'] = ';'.join(address)
        yield item

        for i in range(len(address)):
            yield Request(url = address[i], callback=self.parse_body, dont_filter=True)


    def parse_body(self, response):
        # content = response.xpath("//body//text()").extract()
        # content1 = response.xpath("//body//script//text()").extract()
        # content1 += response.xpath("//body//style//text()").extract()
        # content = [x for x in content if x not in content1]
        
        # content = list(map(lambda x: re.sub(r'[\\n \\r \\t]','',x.strip()), content))
        # content = list(filter(None, content))
        # contentItem['content'] = ';'.join(content)

        contentItem = linkBodyItem()
        # body:二进制类型   text:string类型      包含' \r \n \t \
        tmp = response.text
        tmp = re.sub(r'\n', '', tmp)
        tmp = re.sub(r'\r', '', tmp)
        tmp = re.sub(r'\t', '', tmp)
        tmp = re.sub(r'"', "'", tmp)
        tmp = html.unescape(tmp)
        tmp = re.sub(r'gb2312', 'utf-8', tmp)

        pattern = re.compile(r'<script.*?</script>')
        tmp = pattern.sub(r'', tmp)
        pattern = re.compile(r'<scip.*?</scip>')
        tmp = pattern.sub(r'', tmp)

        contentItem['content'] = tmp
        contentItem['address'] = response.url

        str2 = ""
        if "baike.baidu.com" in response.url:
            contentItem['intro'] = ''.join(response.xpath('//div[@class="lemma-summary"]/div[@class="para"]/text()[1]').extract())
        elif "wikipedia.org" in response.url:                   
            contentItem['intro'] = ''.join(response.xpath('//div[@id="mw-content-text"]/div/p[1]//text()').extract())
        elif 'facebook.com' in response.url:
            str1 = response.url
            k = str1.find('/', 25)
            m = str1.find('/', 8)
            str2 = str1[:m+1] + 'pg' + str1[m:k+1] + 'about/'
            contentItem['intro'] = str2
        elif 'twitter.com' in response.url:
            # //*[@id="react-root"]/div/div/div/main/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div//text()  登录
            # //*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p//text()   未登录
            contentItem['intro'] = ''.join(response.xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p//text()').extract())
        else:
            contentItem['intro'] = " "

        yield contentItem
        if str2 !="":
            yield Request(url = str2, callback=lambda response, address = str1: self.parse_facebook_intro(response, address), dont_filter=True)

    def parse_facebook_intro(self, response, address):
        facebookintroItem = facebookIntroItem()
        facebookintroItem['address'] = address
        facebookintroItem['intro'] = ''.join(response.xpath('//*[@id="PagesProfileAboutInfoPagelet_152100711485335"]/div[3]/div[1]/div/div[3]//div[@class="_5aj7 _3-8j"]//text()').extract())
        yield facebookintroItem
        
        
    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.start_urls + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page':page},dont_filter=True)

