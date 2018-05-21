# _*_ coding:utf-8 _*_
class Person(object):

    __count = 0

    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')
#这里访问不到
print Person.__count