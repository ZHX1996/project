d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for score in d.itervalues():
    sum += score
print sum/len(d)
