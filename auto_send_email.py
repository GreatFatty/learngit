import smtplib, mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def automail(to_addrs = '', cc_addrs = [], title = '', text = '', doc_path = '', doc_name = '', server = 'smtp.126.com', username = '', password = ''):
    try:
        from_addr = username

        mailserver = smtplib.SMTP()
        mailserver.connect('smtp.126.com', 25)
        mailserver.login(username, password)

        message = MIMEMultipart('mixed')
#         if len(cc_addrs) > 0:
#             message = "From: %s\r\n" % from_addr
#                         + "To: %s\r\n" % to_addrs
#                         + "CC: %s\r\n" % ",".join(cc_addrs)
#                         + "Subject: %s\r\n" % title
#                         + "\r\n" 
#                         + text
        text_plain = MIMEText(text, 'plain', 'utf-8')
        message.attach(text_plain)
        message['Subject'] = title
        message['From'] = from_addr
        message['To'] = to_addrs

        
        ctype, encoding = mimetypes.guess_type(doc_path + doc_name)
        maintype, subtype = ctype.split('/', 1)
        text_att = MIMEBase(maintype, subtype)
        file = open(doc_path + doc_name, 'rb')
        sendfile = file.read()
        file.close()
        text_att.set_payload(sendfile)
        encoders.encode_base64(text_att)
        text_att.add_header("Content-Disposition", "attachment", filename = doc_name)
        message.attach(text_att)

        mailserver.sendmail(from_addr, [to_addrs] + cc_addrs, message.as_string())
        mailserver.quit()
        return True
    except:
        print('Send email failed!!!')
        return False


server = 'smtp.126.com'
username = 'baokaimath@126.com'
password = 'GuShen540621Math'
to_addrs = 'zhangbaokai@swutech.cn'
# cc_addrs = ['baokaimath@126.com', 'baokai_zhang@hotmail.com']
cc_addrs = []

doc_path = 'D:\\'
doc_name = r'previous.release-1.6.0-rc3 - 副本.zip'
text = 'Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com'
title = 'How are you'

automail(to_addrs, cc_addrs, title, text, doc_path, doc_name, server, username, password)