import urllib.parse
import urllib.request
import http.cookiejar

filename = 'cookie01.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
postdata = urllib.parse.urlencode({
    'stuid':'1016041218',
    'pwd':'115637'
}).encode('UTF-8')
loginUrl = 'http://ids6.njupt.edu.cn/authserver/login?service=http://my.njupt.edu.cn/login.do'
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
gradeUrl = 'http://yjs.njupt.edu.cn/epstar/web/swms/mainframe/home.jsp'
result = opener.open(gradeUrl)
print (result.read())