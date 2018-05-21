import smtplib  #发不出去
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.header import Header  
from email.utils import formataddr, parseaddr
from email.mime.base import MIMEBase
from email import encoders

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

sender = 'zhi1365370292@sina.com'  
receiver = '1365370292@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.sina.com'  
username = 'zhi1365370292@sina.com'  
password = 'love.no.1' 

msg = MIMEMultipart('related')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = _format_addr('<%s>' % sender)
msg['To'] = _format_addr('<%s>' % receiver)

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))  #发送附件
#msg.attach(MIMEText('<html><body> <p><img src="cid:image1"></p></body></html>','html','utf-8')) #发送图片

with open('F:\\图片\\qq名片\\1.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='1.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='1.jpg')
    mime.add_header('Content-ID', '<image1>')
    mime.add_header('X-Attachment-Id', 'image1')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver, 25) 
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  