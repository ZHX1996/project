import requests
import json

# response = requests.get("http://www.baidu.com")
# print(response.status_code)
# # 使用text时，requests会使用其推测的文本编码
# print(response.text)
# print(response.content)
# print(response.content.decode('utf-8'))
# print(response.cookies)

# requests.post("http://httpbin.org/post")
# requests.put('http://httpbin.org/put')
# requests.delete("http://httpbin.org/delete")
# requests.head("http://httpbin.org/get")
# requests.options("http://httpbin.org/get")

# GET请求
# response = requests.get("http://httpbin.org/get?name=zhx&age=22")
# response.encoding = 'utf-8'
# print(response.text)

# 用params参数传递参数，如果参数为None则不会添加到URL里
# data = {
#     "name":"zhx",
#     "age":22
# }
# response = requests.get("http://httpbin.org/get", params=data)

# 解析json, 一样的效果
# print(response.json())
# print(json.loads(response.text))

# 添加headers
# headers= {
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
# }
# response = requests.get('https://www.zhihu.com', headers = headers)
# print(response.content.decode('utf-8'))

# POST中添加参数
# data = {
#     'name': 'zhx',
#     'age': 22
# }
# response = requests.post("http://httpbin.org/post", data = data)

# 文件上传
# files = {"files":open("cookie.txt", "rb")}
# response = requests.post("http://httpbin.org/post", files=files)

# 会话维持
# 两次请求都通过session对象访问
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)

# 证书验证
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get("https://www.12306.cn", verify=False)
# print(response.status_code)

# 代理设置
# 代理通过proxies参数传递

# 用户认证
# from requests.auth import HTTPBasicAuth
# response = requests.get("http://120.27.34.24:9001/", auth=HTTPBasicAuth("user", "123"))

