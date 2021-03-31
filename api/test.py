# -*- coding: UTF-8 -*-
import configparser
def test(*args,**kwargs):
    print(args) 
    print(kwargs["a"])

def test2(*args,**kwargs):
    test(*args,**kwargs)
    # test()

if __name__ == "__main__":
    # test2(1,2,3,4,a=3,b=6)
    # cf = configparser.ConfigParser()
    # cf.read('../conf/application.conf') 
    # secs = cf.sections()
    # options = cf.options("email")
    # mail_host=cf.get("email", "mail_host")
    # print(mail_host)
    cf = configparser.ConfigParser()
    cf.read('../conf/application.conf')

    # 每个section由[]包裹
    secs = cf.sections()

    # 获取某个section名为prod所对应的键
    options = cf.options("email")

    # 获取[prod]中host对应的值
    host = cf.get("email", "mail_host")
    print(host)
