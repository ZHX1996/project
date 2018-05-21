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
   
f = open('F:\\图片\\qq名片\\3.jpg', 'rb')
att = MIMEText(f.read(), 'plain', 'utf-8') 
f.close() 
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = "attachment; filename='1.jpg'"
msgRoot.attach(att)  
          
smtp = smtplib.SMTP()  
smtp.connect(smtpserver, 25)  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit()  