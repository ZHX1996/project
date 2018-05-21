import functools

sorted_ignore_case = functools.partial(sorted, cmp=lambda s1,s2:cmp(s1.upper(),s2.upper()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])


int2 = functools.partial(int, base=2)
print int2('1000000')