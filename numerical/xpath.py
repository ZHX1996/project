#-*-coding:utf-8-*-
from lxml import etree
sample = '''
<html> 
  <head> 
    <title>My page</title> 
  </head> 
  <body> 
    <h2>Welcome to my <a href="#" src="x">page</a></h2> 
    <p>This is the first paragraph.</p> 
    <!-- this is the end --> 
  </body> 
</html> 
'''
selector = etree.HTML(sample)
# 绝对路径取内容
a = selector.xpath('//title/text()')
# 相对路径取内容
b = selector.xpath('/html/head/title/text()')
print(a, b)

# 获取属性
c = selector.xpath('//h2/a/@src')
d = selector.xpath('//@href')
print(c, d)

# 取出所有文本内容
e = selector.xpath('//text()')
print(e)

# 获取注释
f = selector.xpath('//comment()')
print(f)


sample2 = """ 
<html> 
<body> 
<ul> 
<li>Quote 1</li> 
<li>Quote 2 with <a href="...">link</a></li> 
<li>Quote 3 with <a href="...">another link</a></li> 
<li><h2>Quote 4 title</h2> ... </li> 
</ul> 
</body> 
</html> 
"""
s2 = etree.HTML(sample2)
# 获取li标签下的内容
g = s2.xpath('//ul/li/text()')
print(g)

# 获取第一个li的内容
h = s2.xpath('//li[1]/text()')
print(h)

# 获取前两个li的内容
i = s2.xpath('//li[position()<3]/text()')
print(i)

# 获取奇数位的li
j = s2.xpath('//li[position() mod2=1]/text()')
print(j)

# 获取最后一个li
k = s2.xpath('//li[last()]/text()')
print(k)

# 获取倒数第二个li
l = s2.xpath('//li[last()-1]/text()')
print(l)

# 获取有子标签a的li标签的内容
m = s2.xpath('//li[a]/text()')
print(m)

# 获取有属性href的a标签的内容
n = s2.xpath('//a[@href]/text()')
print(n)

n1 = s2.xpath('//a[@href="..."]/text()')
print('n1', n1)

# 获取有a或h2子标签的li的内容
o = s2.xpath('//li[a or h2]/text()')
print(o)

# 获取所有a和h2标签的内容
p = s2.xpath('//a/text() | //h2/text()')
print(p)

sample3 = u""" 
<html> 
  <head> 
    <title>My page</title> 
  </head> 
  <body> 
    <h2>Welcome to my <a href="#" src="x">page</a></h2> 
    <p>This is the first paragraph.</p> 
    <p class="test"> 
    编程语言<a href="#">python</a> 
    <img src="#" alt="test"/>javascript 
    <a href="#"><strong>C#</strong>JAVA</a> 
    </p> 
    <p class="content-a">a</p> 
    <p class="content-b">b</p> 
    <p class="content-c">c</p> 
    <p class="content-d">d</p> 
    <p class="econtent-e">e</p> 
    <p class="heh">f</p> 
    <!-- this is the end --> 
  </body> 
</html> 
"""
s3 = etree.HTML(sample3)
# 获取某个标签下的所有文本
q = s3.xpath('string(//p[@class="test"])').strip()
print(q)

# 获取p标签下class以content开头的文本
r = s3.xpath('//p[starts-with(@class, "content")]/text()')
print(r)

# 获取p标签下class包含content的文本
s = s3.xpath('//p[contains(@class, "content")]/text()')
print(s)

# 其他还有(text(), "content")    (@src, "content")



