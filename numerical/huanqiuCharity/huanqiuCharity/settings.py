# -*- coding: utf-8 -*-

# Scrapy settings for huanqiuCharity project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'huanqiuCharity'

SPIDER_MODULES = ['huanqiuCharity.spiders']
NEWSPIDER_MODULE = 'huanqiuCharity.spiders'

DOWNLOAD_DELAY = 3
RETRY_TIMES = 5

ITEM_PIPELINES = {
    'huanqiuCharity.pipelines.Pipeline_ToCSV': 100
}

# DEFAULT_REQUEST_HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.0.1594 Safari/537.36'
#  }

DOWNLOADER_MIDDLEWARES = {
    'huanqiuCharity.middlewares.ProxyMiddleware' : 543,
}

PROXIES = ['187.63.82.55:51769', '118.172.201.45:34670', '177.92.160.254:54868', '205.185.115.100:8080', '102.177.96.118:61130', '112.85.128.138:9999', '52.23.208.184:80', '116.62.222.99:3128', '125.62.213.33:83', '27.204.86.160:9999', '145.239.169.42:8080', '101.132.193.192:8118', '118.31.56.152:3128', '116.62.234.0:3128', '111.231.92.21:8888', '118.31.61.199:3128', '203.176.132.110:8080', '103.75.34.121:38324', '88.247.192.105:42045', '182.253.142.13:3128', '201.236.200.242:8080', '181.214.240.175:3129', '41.87.29.130:8080', '122.154.97.188:8080', '180.179.13.135:80', '165.16.55.12:83', '177.184.83.235:20183', '59.91.121.161:51445', '36.91.129.164:8080', '59.152.90.109:8080', '187.45.123.118:8080', '118.174.232.237:48665', '195.211.174.36:56746', '37.187.121.205:3128', '202.153.231.150:3128', '170.210.236.1:57182', '170.82.230.54:8080', '77.45.111.74:60800', '86.123.166.109:8080', '203.201.149.69:80', '169.255.191.218:8080', '176.192.35.2:61800', '179.43.81.135:80', '223.197.161.249:8080', '103.233.152.140:8080', '42.115.88.71:62225', '45.160.7.73:8081', '134.119.188.154:8080', '185.255.46.100:30678', '195.234.210.48:51545', '190.52.193.100:80', '103.75.161.38:21776', '1.20.99.218:36117', '111.118.128.140:41344', '45.232.247.210:8080', '95.80.252.189:52371', '62.24.109.89:60045', '116.62.240.1:3128', '202.21.124.226:41258', '87.244.176.213:58893', '103.111.199.19:8080', '46.45.19.138:53281', '134.119.205.246:8080', '180.250.247.126:23500', '36.66.107.219:3128', '181.44.133.155:8080', '49.51.70.42:1080', '181.209.86.133:999', '41.203.75.194:8080', '116.66.197.210:8080', '72.38.188.134:38688', '103.42.254.110:37861', '103.78.248.94:8080', '197.211.245.50:53281', '217.182.51.227:1080', '96.9.73.177:8080', '36.71.150.87:8080', '68.15.151.20:48678', '41.139.184.250:8080', '123.206.103.161:1080', '177.67.143.179:47998', '177.36.183.157:8080', '103.57.70.248:31203', '36.255.87.236:83', '212.42.113.240:60873', '217.150.77.31:53281', '103.83.94.218:808', '200.170.143.155:8080', '95.154.106.164:35609', '58.97.72.83:8080', '103.102.67.65:63141', '186.148.190.78:999', '5.1.104.98:38144', '43.225.185.146:8080', '94.191.112.220:80', '95.181.130.149:35689', '181.40.84.38:49674', '89.24.124.83:36665', '182.53.206.163:61111', '36.67.239.23:8080']

AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.0.1594 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    "Mozilla/2.02E (Win95; U)",
    "Mozilla/3.01Gold (Win95; I)",
    "Mozilla/4.8 [en] (Windows NT 5.1; U)",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)"
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huanqiuCharity (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'huanqiuCharity.middlewares.HuanqiucharitySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'huanqiuCharity.middlewares.HuanqiucharityDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'huanqiuCharity.pipelines.HuanqiucharityPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
