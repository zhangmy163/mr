# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import configparser
from pathlib import Path

base_dir=Path(__file__).resolve().parent
conf_dir=str(base_dir.parent)+"/conf"
conf_mappingfile=conf_dir+"/emailmapping.conf"
conf_appfile=conf_dir+"/application.conf"

class sendEM():
    def _get_config(self):
        cf = configparser.ConfigParser()
        cf.read(conf_appfile) 
        self.secs = cf.sections()
        self.options = cf.options("email")
        self.mail_host=cf.get("email", "mail_host")
        self.mail_user=cf.get("email", "mail_user")
        self.mail_pass=cf.get("email", "mail_pass")
        self.sender = cf.get("email", "mail_user")
        print(self.mail_host)

    def get_config(self,op):
        self._get_config()
        cf = configparser.ConfigParser()
        cf.read(conf_mappingfile) 
        self.secs = cf.sections()
        self.options = cf.options(op)
        self.receivers = cf.get(op, "receivers")


    def sendmsg(self,channel,subject,content):
        self.get_config(channel)
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("邮件服务", 'utf-8')
        message['To'] =  Header("测试", 'utf-8')

        subject = subject
        message['Subject'] = Header(subject, 'utf-8')
        print(self.mail_host)
        print(self.mail_user)
        print(self.mail_pass)
        print(self.sender)
        print(self.receivers)
        print(message.as_string())

        # try:
        #     smtpObj = smtplib.SMTP() 
        #     smtpObj.connect(self.mail_host, 25)    # 25 为 SMTP 端口号
        #     smtpObj.login(self.mail_user,self.mail_pass)  
        #     smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        #     print( "邮件发送成功")
        # except smtplib.SMTPException:
        #     print( "Error: 无法发送邮件")

if __name__ == "__main__":
    a = sendEM()
    # a._get_config()
    a.sendmsg("imedia","测试主题","测试内容")