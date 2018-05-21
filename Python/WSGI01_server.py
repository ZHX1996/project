from wsgiref.simple_server import make_server
from WSGI01_hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 80000...')
httpd.serve_forever()