import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 80))
s.listen(1)
while True:
	cs, ca = s.accept()
	print cs.recv(1024)
	cs.sendall('replay')
	cs.close()