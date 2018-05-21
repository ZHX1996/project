def calc_prod(lst):
    def lazy_multiply():
        def f(x, y):
            return x * y
        return reduce(f,lst,1)
    return lazy_multiply

f = calc_prod([1, 2, 3, 4])
print f()