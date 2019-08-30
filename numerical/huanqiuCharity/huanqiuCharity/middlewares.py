# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import scrapy
import random
import requests
from bs4 import BeautifulSoup

# class ProxyMiddleware(object):
#     def __init__(self):
#         header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.0.1594 Safari/537.36',
#         'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWE1YWRhODI1OGUyOTI1NTU4MTBhZDBiZGY5NjVlYWMzBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVdBeDNMblk3THBtbmxIVjRDLzVPSlQvR0pQZWJHMzNRaVcwVVFtTXluTWM9BjsARg%3D%3D--9ca25195661b18461d1bee2b41b525ff60023079'
#         }

#         url = 'https://www.xicidaili.com/nt/'

#         response = requests.get(url, headers=header)
#         soup = BeautifulSoup(response.text, 'lxml')
#         ips = soup.select('table tr')
#         ips.remove(ips[0])
#         ip_list = []
#         for i in ips:
#             for j, k in enumerate(i):
#                 if j == 3:
#                     port = k.find_next_sibling().get_text()
#                     ip = k.get_text()
#                     ip_list.append(ip + ':' + port)
#         self.ip = ip_list

#     # @classmethod
#     # def from_crawler(cls, crawler):
#     #     return cls(ip=crawler.settings.get('PROXIES'))

#     def process_request(self, request, spider):
#         print(self.ip)
#         request.meta['proxy'] = 'http://' + random.choice(self.ip)


class ProxyMiddleware(object):
    def __init__(self, ip, user_agent):
        self.ip = ip
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(ip=crawler.settings.get('PROXIES'),user_agent=crawler.settings.get('AGENTS'))


    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://' + random.choice(self.ip)
        request.headers['User-Agent'] = random.choice(self.user_agent)



class HuanqiucharitySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HuanqiucharityDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
