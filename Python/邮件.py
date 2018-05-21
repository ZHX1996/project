import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
from email.utils import formataddr, parseaddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
  
sender = 'zhi1365370292@sina.com'  
receiver = '1365370292@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.sina.com'  
username = 'zhi1365370292@sina.com'  
password = 'love.no.1'  
  
#msg = MIMEText('你好','plain','utf-8') 
msg = MIMEText('''<html><body><h1>Hello</h1>
     <p><a href="http://www.python.org">Python</a>...</p>
     </body></html>''', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = _format_addr('<%s>' % sender)
msg['To'] = _format_addr('<%s>' % receiver) 
  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver, 25) 
#smtp.ehlo()  smtp.starttls()  smtp.ehlo()    #SSL安全连接时
#smtp.set_debuglevel(1)  #显示交互信息
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  