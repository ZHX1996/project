from datetime import datetime, timedelta

now = datetime.now()
print (now)
print ('\n')

ti = datetime(2015, 1, 1, 12, 30, 25)
ti01 = ti.timestamp()
print (ti)
print (ti01)
print (datetime.fromtimestamp(ti01))
print (datetime.utcfromtimestamp(ti01))
print ('\n')

# str to datetime
str01 = '2015-6-1 18:19:59'
cday = datetime.strptime(str01,  '%Y-%m-%d %H:%M:%S')
print (cday)

#datetime to str
print(now.strftime('%a, %b %d %H:%M'))

print(now + timedelta(days = 2, hours = 12))