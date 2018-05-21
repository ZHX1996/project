# _*_ coding:utf-8 _*_
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score  #__开头无法被外部访问

p = Person('Bob', 59)

print p.name
print p.__score