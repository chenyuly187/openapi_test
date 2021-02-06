# -*- coding: utf-8 -*-
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.application import MIMEApplication

file = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '/files/case.xlsx'

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def sendMail():
    '''输入邮箱地址'''
    from_addr = "15021847009@163.com"
    password = 'lysh471000'
    # 输入收件人地址
    to_list = ['1178821890@qq.com']
    # 输入SMTP服务器地址
    smtp_server = 'smtp.163.com'

    msg = MIMEMultipart()
    msg['From'] = _format_addr(' <%s> '%from_addr)
    msg['To'] = ','.join(to_list)
    msg['Subject'] = Header(u'测试结果','utf-8').encode()
    '''邮件正文是MIMEText'''
    msg.attach(MIMEText('验证qq邮箱是否可以接收到邮件','plain','utf-8'))
    '''xlsx 类型附件'''
    part = MIMEApplication(open(file,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename='test_result.xlsx')
    msg.attach(part)

    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.starttls()
    server.login(from_addr,password)
    server.sendmail(from_addr,to_list,msg.as_string())
    server.quit()


if __name__ == "__main__":
    sendMail()