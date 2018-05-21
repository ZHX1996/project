import re
s = "hello, csvt"
print s.replace('csvt', 'python')

rs = r'c..t'
print re.sub(rs, 'python', 'csvt caat cvvt cccc')
print re.subn(rs, 'python', 'csvt caat cvvt cccc')