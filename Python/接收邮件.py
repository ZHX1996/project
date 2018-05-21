import poplib 
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from email.message import Message

class POP3:
    def __init__(self, charset = 'utf-8'):
        self.charset = charset

    def connect(self, from_server):
        self.pop = poplib.POP3_SSL(from_server) 
        self.pop.set_debuglevel(1)
        print(self.pop.getwelcome().decode(self.charset))

    def validate(self, from_addr, from_pass):
        self.pop.user(from_addr) 
        self.pop.pass_(from_pass) 

    def getmail(self):
        #(message count, mailbox size)
        count, size = self.pop.stat()
        print('counts: <%s>; size: <%s>' % (count, size))

        #(response, ['mesg_num octets', ...], octets)''])
        resp, mails, octets = self.pop.list()
        for x in range(len(mails)):
            try:         
                resp, lines, octets = self.pop.retr(len(mails)-x)
                msg = b'\r\n'.join(lines).decode(self.charset)
                self.print_info(Parser().parsestr(msg))
            except Exception as e:
                print(e)

    def close(self):
        self.pop.quit()
        print("close connection!")


    def print_info(self, msg, indent=0):
        if indent == 0:
            for header in ['From', 'To', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header=='Subject':
                        value = self.decode_str(value)
                    else:
                        hdr, addr = parseaddr(value)
                        name = self.decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
                print('%s%s: %s' % ('  ' * indent, header, value))
        if (msg.is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                print('%spart %s' % ('  ' * indent, n))
                print('%s--------------------' % ('  ' * indent))
                self.print_info(part, indent + 1)
        else:
            content_type = msg.get_content_type()
            if content_type=='text/plain' or content_type=='text/html':
                content = msg.get_payload(decode=True)
                charset = self.guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                print('%sText: %s' % ('  ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % ('  ' * indent, content_type))

    def decode_str(self, s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    def guess_charset(self, msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset


def main():
    from_addr = '1365370292@qq.com'
    from_pass = 'ltxaepgctcqqfhbe'
    from_server = 'pop.qq.com'

    pop = POP3()
    pop.connect(from_server)
    pop.validate(from_addr, from_pass)
    pop.getmail()


if __name__ == '__main__':
    main()