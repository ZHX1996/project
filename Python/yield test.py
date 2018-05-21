def gen():
    a = yield 1
    print('yield a % s' % a)
    b = yield 5
    print('yield b % s' % b)
    c = yield 9
    print('yield c % s' % c)


r = gen()
x = next(r)
print('next x %s' % x)
y = r.send(10)
print('next y %s' %y)
z = next(r)
print('next z %s' % z)
e = r.send(88)