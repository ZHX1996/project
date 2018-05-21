import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
  
sender = 'zhi1365370292@sina.com'  
receiver = '1365370292@qq.com'   
smtpserver = 'smtp.sina.com'  
username = 'zhi1365370292@sina.com'  
password = 'love.no.1'  
  
msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = 'test message'  
  
msgText = MIMEText('<html><body><h1>Hello</h1><p><img src="cid:image1"></p></body></html>','html','utf-8')  
msgRoot.attach(msgText)  
  
f = open('F:\\图片\\qq名片\\3.jpg', 'rb') 
msgImage = MIMEImage(f.read())  
f.close()  
msgImage.add_header('Content-ID', '<image1>')  
msgRoot.attach(msgImage)  
  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver, 25)  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit()  