import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 80))

print (c.send('hello'))
print (c.recv(1024))
c.close()