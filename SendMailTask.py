#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="设置SMTP服务器"  #设置服务器
mail_user="用户ID"    #用户名
mail_pass="用户密码"   #口令
  
sender = '发送邮件地址'
receivers = ['接受邮件地址']  # 接收邮件，可设置为ß你的QQ邮箱或者其他邮箱

# message = MIMEText('邮件内容', 'plain', 'utf-8')
# message['From'] = Header("xxxx@xxx.com", 'utf-8')
# message['To'] =  Header("xxxx@xxx.com", 'utf-8')

# 网上搜到的程序大多是以上的内容。我自己在测试过程中发现这样发送，高概率会被smtp服务器识别为垃圾邮件。
# 如果你是像我一样只是为了一些目的用邮件通知自己，不妨简单一些。

message = MIMEText('正在进行的作业（' + sys.argv[1] + '）已经结束')
message['From'] = Header("发送邮件地址")
message['To'] =  Header("接受邮件地址")

subject = '正在进行的作业（' + sys.argv[1] + '）已经结束'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
