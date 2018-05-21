import re

s = """hhsd hello src=csvt yes jdjds
dsjdh src=123 yes jflsm
hello src=python yes ksa"""

r1 = r'hello src=(.+) yes'
r2 = r'hello src=.+ yes'

print re.findall(r1, s)
print re.findall(r2, s)