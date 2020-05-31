#!/usr/bin/python
# -*- encoding=utf-8 -*-


import os
import django
import smtplib
from backend import settings
from email.mime.text import MIMEText

from django.core import mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


def send_mail():
    title = 'test django email'
    content = 'hello django mail'
    receivers = ['3391217495@qq.com']
    status = mail.send_mail(subject=title, message=content,
                            from_email=settings.EMAIL_FROM, recipient_list=receivers)
    print(status)

def send_mail_native():
    msg = MIMEText("邮件通道测试", "plain", 'utf-8')
    msg['FROM'] = "Mail Test"
    msg['Subject'] = "【Mail Test】"
    receivers = ['3391217495@qq.com']
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()

if __name__ == '__main__':
    send_mail()
