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

ITEM_PIPELINES = {
    'huanqiuCharity.pipelines.Pipeline_ToCSV': 100
}

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.0.1594 Safari/537.36'
 }

DOWNLOADER_MIDDLEWARES = {
    'huanqiuCharity.middlewares.ProxyMiddleware' : 543,
}

PROXIES = ['220.158.236.40:3128', '186.225.106.114:46312', '216.255.170.14:48678', '91.135.242.10:8080', '198.50.172.160:1080', '93.190.139.150:8080', '186.46.184.182:8080', '49.156.43.95:8080', '124.41.211.82:45024', '186.5.117.18:3128', '181.129.133.74:56827', '221.226.94.218:110', '181.129.141.210:41849', '129.205.201.27:46479', '46.229.67.198:47437', '182.253.193.210:32128', '189.89.248.40:3128', '123.206.103.161:1080', '195.211.160.88:44464', '187.163.36.54:35611', '160.19.246.180:56482', '81.1.213.36:8080', '46.101.1.221:80', '197.149.128.25:8080', '185.132.178.137:1080', '46.185.78.25:8080', '86.110.189.118:56710', '167.86.92.144:3128', '83.239.151.138:45494', '190.217.80.252:8080', '198.11.178.14:8080', '192.99.191.235:1080', '118.174.165.229:8080', '187.17.146.25:8080', '206.72.203.42:80', '58.16.7.37:52284', '202.143.121.245:8080', '18.202.26.136:3128', '112.12.91.20:8888', '191.102.82.91:9991', '103.13.231.113:8080', '80.28.243.202:52267', '197.255.152.43:48105', '82.100.4.63:44348', '103.196.233.199:8080', '185.132.178.203:1080', '201.182.97.90:3128', '181.133.180.2:60051', '110.164.58.106:8082', '202.79.25.246:37146', '49.128.181.13:8081', '183.247.152.98:53281', '102.129.72.18:8080', '41.33.22.186:80', '154.72.79.252:57768', '84.47.136.146:8080', '167.249.181.191:3128', '185.132.178.201:1080', '83.168.85.35:8090', '103.243.82.227:33727', '169.239.223.136:44267', '124.206.242.127:3128', '195.46.168.147:8080', '190.144.51.114:8080', '169.255.136.14:45743', '177.93.96.137:8080', '176.212.127.1:37071', '103.134.41.58:8080', '95.158.63.46:44405', '85.21.63.219:53281', '181.176.161.213:61840', '122.248.45.35:53281', '1.179.164.233:43244', '119.15.93.4:8080', '185.132.178.207:1080', '124.41.211.211:45557', '5.133.24.121:8888', '89.151.141.246:33712', '193.68.26.185:44682', '51.158.97.225:3128', '1.197.203.112:9999', '1.198.73.80:9999', '120.29.124.131:8080', '170.247.156.71:8080', '217.182.120.165:1080', '202.21.101.130:45093', '91.211.122.23:39784', '186.211.248.214:44385', '194.44.61.10:44066', '199.195.248.24:8080', '210.4.120.246:8080', '51.15.112.24:8080', '95.79.55.196:53281', '93.190.137.26:8080', '93.190.137.122:8080', '103.87.236.46:41183', '198.50.172.165:1080', '35.199.74.103:80', '41.180.47.42:8080', '202.61.49.52:44317']

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
