# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyGoogleSearch.items import ScrapygooglesearchItem, linkBodyItem
from scrapy.shell import inspect_response
import re


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['www.google.com']
    start_urls = 'https://www.google.com/search?q='


    def parse(self, response):
        # inspect_response(response, self)

        products = response.xpath('//div[@id="rso"]/div/div[contains(@class,"srg")]/div[contains(@class,"g")]')
        for product in products:
            address = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/@href').extract()
            title = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/h3/text()').extract()
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
        # body:二进制类型   text:string类型      包含' \r \n \t \'
        contentItem['content'] = response.text 
        contentItem['address'] = response.url
        yield contentItem

                                                                                    
    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.start_urls + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page':page},dont_filter=True)

