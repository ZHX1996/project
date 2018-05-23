from bs4 import BeautifulSoup

# <p class="title"><b>The Dormouse's story</b></p>
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a> and
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
# 修饰
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id="link3"))

# for link in soup.find_all('a'):
#     print(link["href"])

# print(soup.get_text)
#子节点和子孙节点
# print(soup.p.contents)

# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(child)
#
# for j, descentdant in enumerate(soup.p.descendants):
#     print(descentdant)

# 兄弟节点
# next_siblings 后面的兄弟节点
# next_sibling 下一个兄弟标签
# previous_siblings 前面的兄弟节点
# previous_sibling 上一个兄弟标签
# for i, brother in enumerate(soup.a.next_siblings):
#     print(brother)
# 获得的是a标签后面的值
# print(soup.a.next_sibling)

html1='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup1 = BeautifulSoup(html1, 'lxml')

# find_all
# print(soup1.find_all('ul'))

# for ul in soup1.find_all('ul'):
#     print(ul.find_all('li'))

# attr
# print(soup1.find_all(attrs={'id': 'list-1'}))
# print(soup1.find_all(attrs={'name': 'elements'}))
# print(soup1.find_all(attrs={'class': 'element'}))

# text
# print(soup1.find_all(text='Foo'))
# for i in soup1.find_all(text='Foo'):
#     print(i.parent)

# CSS选择器
for li in soup1.select('li'):
    print(li.get_text())

for ul in soup1.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])