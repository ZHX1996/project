import re
f1 = open("C:\\Users\\Administrator\\Desktop\\1.txt", 'r')
s = r'hello'
list1 = re.findall(s,f1.read())
f1.close()
print len(list1)