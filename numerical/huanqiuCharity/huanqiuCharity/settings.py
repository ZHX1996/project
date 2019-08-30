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

DOWNLOAD_DELAY = 5
RETRY_TIMES = 10

ITEM_PIPELINES = {
    'huanqiuCharity.pipelines.Pipeline_ToCSV': 100
}

# DEFAULT_REQUEST_HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.0.1594 Safari/537.36'
#  }

DOWNLOADER_MIDDLEWARES = {
    'huanqiuCharity.middlewares.ProxyMiddleware' : 543,
}

PROXIES = ['95.86.48.148:33304', '73.216.132.208:44428', '27.208.138.70:8060', '113.53.82.92:39726', '138.201.223.250:31288', '91.150.189.122:57138', '210.212.68.209:39657', '77.242.16.26:53281', '170.80.156.42:8080', '181.112.42.38:38264', '209.80.12.182:80', '110.172.135.234:43635', '51.38.71.101:8080', '171.100.209.38:8080', '5.133.27.150:8080', '93.190.137.122:1080', '36.83.93.253:80', '103.24.135.49:8080', '128.199.254.103:23352', '114.104.141.162:808', '103.36.81.19:49654', '103.108.88.206:8080', '35.240.139.161:8080', '82.151.114.197:56208', '119.18.147.111:8080', '200.13.154.29:8080', '43.249.41.7:42163', '197.148.64.194:8080', '154.72.76.246:8080', '190.14.249.138:9991', '223.85.196.75:9797', '183.88.252.56:8080', '191.6.25.69:20183', '158.69.138.13:1080', '190.61.39.33:9991', '181.176.161.213:61840', '36.89.228.201:44342', '36.91.143.58:8080', '36.92.90.28:8080', '62.176.126.66:35830', '105.112.8.53:3128', '115.171.202.128:9000', '191.98.222.2:6666', '119.235.53.135:33740', '186.148.168.94:33019', '116.197.134.222:8080', '45.76.87.52:8080', '1.10.189.68:60400', '87.247.3.234:33694', '140.227.161.6:60088', '49.51.195.147:80', '86.110.27.165:3128', '170.84.93.73:36001', '93.190.139.155:8080', '186.192.98.250:8080', '195.116.133.1:33528', '103.69.220.58:8080', '186.103.175.158:3128', '27.72.244.228:8080', '188.225.179.98:51014', '221.2.155.35:8060', '200.35.43.105:52232', '186.46.120.230:57497', '41.169.11.210:45088', '187.63.111.37:3128', '202.57.62.170:49910', '96.9.79.219:8080', '210.5.10.87:53281', '36.255.87.247:83', '128.201.97.155:53281', '103.108.90.18:48330', '62.176.12.111:8080', '190.63.144.41:46881', '46.33.253.29:45114', '103.41.212.186:8080', '45.112.127.23:8080', '103.79.164.61:53281', '42.115.19.2:8080', '143.202.199.66:999', '195.225.142.205:38494', '62.218.24.135:80', '195.234.210.48:51545', '185.51.213.31:8080', '39.137.168.230:80', '36.89.88.137:3128', '116.90.122.3:8080', '190.5.225.178:31990', '190.128.101.78:8080', '97.72.253.34:87', '200.60.176.99:53281', '177.67.219.1:61416', '81.161.205.4:8080', '193.34.140.84:57220', '188.209.245.255:8080', '36.89.190.85:8080', '116.62.205.241:3128', '51.158.123.35:8811', '60.2.44.182:40268', '140.227.168.6:60088', '190.104.64.242:9090']

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
