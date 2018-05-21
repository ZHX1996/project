from urllib import request

with request.urlopen('https://www.huxiu.com/') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s:%s' % (k,v))
	#print('Data:', data.decode('utf-8').encode('gbk'))
	print(type(data))