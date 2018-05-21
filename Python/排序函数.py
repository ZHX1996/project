print sorted([36, 5, 12, 9, 21])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
	
print sorted([36, 5, 12, 9, 21], reversed_cmp)


print sorted(['bob', 'about', 'Zoo', 'Credit'])


def cmp_ignore_case(s1, s2):
    if s1.lower() < s2.lower():
        return -1
    if s1.lower() > s2.lower():
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)