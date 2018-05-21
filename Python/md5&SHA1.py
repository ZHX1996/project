import hashlib

md5 = hashlib.md5()
md5.update('my name is zhihanxiao'.encode('utf-8'))
md5.update('what is your name?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('my name is zhihanxiao'.encode('utf-8'))
sha1.update('what is your name?'.encode('utf-8'))
print(sha1.hexdigest())
