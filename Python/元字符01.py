# [] ^ $
import re
s1 = r'abc'
print re.findall(s1, 'aaaaaaaaabcaaaaaabcbbbc')

s2 = r't[io]p'
n1 = 'top tip tep t2p tSp'
print re.findall(s2,  n1)

s3 = r't[a-zA-Z0-9]p'
print re.findall(s3, n1)

s4 = r'^hello'
s5 = r'^Hello'
n2 = 'Hello world, hello boy'
print re.findall(s4, n2)
print re.findall(s5, n2)

s6 = r'boy$'
print re.findall(s6, n2)


