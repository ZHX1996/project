import re
f1 = open("C:\\Users\\Administrator\\Desktop\\1.txt", 'r+')
list1 = f1.readlines()
print list1
s = r'csvt'
list2 = []
for i in list1:
	list2.append(re.sub(s, 'hello', i))
	
print list2
f1.seek(0,0)
f1.writelines(list2)
f1.close()