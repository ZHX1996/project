import base64

def safe_base64_decode(s):
	i = (4 - len(s)) % 4
	s = s + '=' * i
	print(s)
	
safe_base64_decode('YWJjZA')