#!/user/bin/python
import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
	
def getImg(html):
#	reg = r'src="(.*?\.jpg)" width'
#	reg = r'src="(.+?jpg)"'
	reg = r'src="(.+jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl, 'D:\\%s.jpg' % x)
		x+=1
#	return imglist 
	
html = getHtml("http://tieba.baidu.com/p/4692434944?fr=ala0&pstaala=2&tpl=5")
print (html)
print getImg(html)