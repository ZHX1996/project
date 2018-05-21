import re
f1 = open("C:\\Users\\Administrator\\Desktop\\1.txt", 'r')
f2 = open("C:\\Users\\Administrator\\Desktop\\2.txt", 'w+')
list1 = f1.readlines()
f2.writelines(list1)

f1.close()
f2.close()

