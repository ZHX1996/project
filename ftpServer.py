import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer

ip = "0.0.0.0"
port = "21"
max_upload = 300*1024
max_download = 300*1024
max_cons = 256
max_pre_ip = 10
enable_logging = True
logging_name = r"ftp.log"
masquerade_address = "127.0.0.1"
welcom_banner = r"welcome to ftp"

def init_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "123456", "D://MyDrivers", perm="elradfmw")  #改变目录 

    dtp_handler = ThrottledDTPHandler
    dtp_handler.read_limit = max_download
    dtp_handler.write_limit = max_upload

    handler = FTPHandler
    handler.authorizer = authorizer

    if enable_logging:
        logging.basicConfig(filename=logging_name, level=logging.INFO)

    handler.banner = welcom_banner
    handler.masquerade_address = masquerade_address

    handler.passive_ports = range(2000, 2333)
    address = (ip, port)
    server = FTPServer(address, handler)
    server.max_cons = max_cons
    server.max_cons_per_ip = max_pre_ip

    server.serve_forever()

if __name__ == '__main__':
    init_ftp_server()