# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
# from pyvirtualdisplay import Display

# 虚拟页面
# from pyvirtualdisplay import Display
# display = Display(visible=0,size=(800,600))
# display.start()
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')

# 关闭图片选项
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chromeOptions.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chromedriver_path,chrome_options=chromeOptions)
# driver.get(url)

class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_extension('./scrapyGoogleSearch/chromeplugin.crx')
        self.chrome_options.add_argument("--user-data-dir="+r"C:/Users/Administrator.SC-201905252025/AppData/Local/Google/Chrome/User Data/")
        prefs = {"profile.managed_default_content_settings.images":2}
        self.chrome_options.add_experimental_option("prefs",prefs)

        # display = Display(visible=0,size=(800,600))
        # display.start()

        self.browser = webdriver.Chrome(service_args=service_args,chrome_options=self.chrome_options)
        # self.browser.set_window_size(1280, 768)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    
    def process_request(self, request, spider):
        self.logger.debug('chrome is starting')
        page = request.meta.get('page', 1)
        try:
            self.browser.get(request.url)
            if page>1:
                nextPage = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div#main div#cnt.mdm div.mw div#rcnt div.col div#center_col div div#foot span#xjs div#navcnt table#nav tbody tr td.navend a#pnnext.pn > span.csb.ch')))
                nextPage.click()
            # self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#nav > tbody > tr > td.cur'), str(page)))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div#main div#cnt.mdm div.mw div#rcnt div.col div#center_col div#res.med div#search div div#rso div div.srg > div.g')))
            return HtmlResponse(url=request.url, body=self.browser.page_source,request=request,encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)


    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),service_args=crawler.settings.get('CHROME_SERVICE_ARGS'))


class ScrapygooglesearchSpiderMiddleware(object):
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


class ScrapygooglesearchDownloaderMiddleware(object):
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
