L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index + 1, '-', name

num = range(1,4)
t = zip(num,L)
for i in t:
	print t[i]