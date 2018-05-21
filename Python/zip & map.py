n1 = [1,3,5]
n2 = [2,4,6]
def mul(x,y):
	return x*y
print zip(n1, n2)
print map(mul, n1, n2)

name = ['tom', 'jane', 'mac']
age = [10, 11]
print map(None, name, age)

lst = range(1,101)
def func(x,y):
	return x+y
print reduce(func, lst, 0)
