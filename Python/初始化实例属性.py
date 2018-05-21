class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, w in kw.iteritems():
            setattr(self, k, w)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student', a = 'b', c = 'd')

print xiaoming.name
print xiaoming.job
print xiaoming.a
print xiaoming.c