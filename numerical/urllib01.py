from urllib import request, parse, error
import socket
from http import cookiejar

# get
# response = request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# post
# data = bytes(parse.urlencode({'word':'hello'}), encoding='utf-8')
# resonse = request.urlopen('http://httpbin.org/post', data=data)
# print(resonse.read().decode('utf-8'))

# timeout
# try:
#     response = request.urlopen('http://httpbin.org/get', timeout=0.1)
# except error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('time out')

# 请求头
# response = request.urlopen('https://python.org')
# print(response.status)
# print(response.getheaders())

# 添加头部信息
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {'name':'zhaofan'}
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# 使用代理
# proxy_handler = request.ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read().decode('utf-8'))

# 得到cookie
# cookie = cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+'='+item.value)

# 保存cookie
# filename = 'cookie.txt'
# cookie = cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 读取cookie
# cookie = cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# 异常处理
# HTTPError是URLError的子类
# URLError只有reason属性，HTTPError有code,reason,headers属性
# try:
#     response = request.urlopen('http://pythonsite.com/111.html')
# except error.HTTPError as e:
#     print(e.code)
#     print(e.reason)
#     print(e.headers)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('rquest successfully')

# URL解析
# result = parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment")
# print(result)
#
# # 拼接
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123', 'commit']
# print(parse.urlunparse(data))
#
# # 拼接
# print(parse.urljoin('http://www.baidu.com', 'FAQ.html'))
#
# # 将字典转化为URL参数
# params = {'name':'zhx', 'age':23}
# base_url = 'http://www.baidu.com?'
# url = base_url + parse.urlencode(params)
# print(url)
