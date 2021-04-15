import json
import urllib3
import configparser
from pathlib import Path

base_dir=Path(__file__).resolve().parent
conf_dir=str(base_dir.parent)+"/conf"
conf_mappingfile=conf_dir+"/ddmapping.conf"

def _send_ding(msg,DING_TOKEN,DING_KEY=None):
    '''
    msg:消息\n
    DING_TOKEN：钉钉机器人token\n
    DING_KEY：机器人要求的关键字，默认是None，如果传入则消息格式为DING_KEY：msg
    '''
    url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(DING_TOKEN)
    http = urllib3.PoolManager(headers={'Content-Type': 'application/json'})

    if DING_KEY is not None:
        msg = '{}: {}'.format(DING_KEY, msg)
    content = dict(content='{}'.format(msg))
    data = dict(msgtype='text', text=content)
    http.request('POST', url, body=json.dumps(data))

def send_ding(op,msg,key=None):
    cf = configparser.ConfigParser()
    cf.read(conf_mappingfile) 
    secs = cf.sections()
    options = cf.options(op)
    token = cf.get(op, "token")

    _send_ding(msg,token,key)

if __name__ == "__main__":
    send_ding("imedia-autorunner","测试信息")