# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyGoogleSearch.items import ScrapygooglesearchItem
from scrapy.shell import inspect_response


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['www.google.com']
    start_urls = 'https://www.google.com/search?q='


    def parse(self, response):
        # inspect_response(response, self)

        products = response.xpath('//div[@id="rso"]/div/div[contains(@class,"srg")]/div[contains(@class,"g")]')
        for product in products:
            # item['address'] = ''.join(product.xpath('//div[@class="rc"]/div[@class="r"]/a/@href').extract()).strip()
            # item['title'] = ''.join(product.xpath('//div[@class="rc"]/div[@class="r"]/a/h3/text()').extract()).strip()
            address = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/@href').extract()
            title = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/h3/text()').extract()
            break

        item = ScrapygooglesearchItem()
        item['title'] = ';'.join(title)
        item['address'] = ';'.join(address)
        yield item

        # for i in range(len(title)):
        #     item = ScrapygooglesearchItem()
        #     item['title'] = title[i]
        #     item['address'] = address[i]
        #     yield item

                                                                                    
    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE')+1):
                url = self.start_urls + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page':page},dont_filter=True)

