#发邮件模板
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
def emails(to_list, zhuti, message_body_utf8):
    msg = MIMEMultipart()
    msg_to_list = to_list
    msg['From'] = 'luzude@funtsui.com'
    Header(msg_to_list, 'utf-8')
    msg['Subject'] = Header('%s'%zhuti, 'utf-8')
    content = "<h2>各位好：</h2><li><font color='red' size='1000'> %s </font></li>"%message_body_utf8
    part = MIMEText(content,'html','utf-8')
    msg.attach(part)
    smtp_server = 'smtp.gmail.com'
    smtp_port = '465'
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.connect('smtp.gmail.com')
    #server.login('luzude@funtsui.com','luzude@1234')
    server.login('zhengming@funtsui.com', 'zhengming')
    server.sendmail(msg['from'],msg_to_list, msg.as_string())
    server.quit()

emails("zhengming@funtsui.com","zhuti","123")
