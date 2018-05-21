L = []
for x in range(1,11):
	L.append(x*x)
print L

print [x*x for x in range(1,11)]
# 1*2 3*4 ...
print [x*(x+1) for x in range(1,100,2)]
