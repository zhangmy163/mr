from flask import Flask  
from flask import request
from flask import redirect
from flask import jsonify
import json5
import configparser

cf = configparser.ConfigParser()
cf.read('./conf/application.conf')

# 每个section由[]包裹
secs = cf.sections()

# 获取某个section名为kafka所对应的键
options = cf.options("kafka")

# 获取[kafka]中host对应的值
ad = cf.get("kafka", "address")
print(ad)

app = Flask(__name__)
@app.route('/send', methods=['GET','POST'])

def send():
    print(request.headers)
    print(request.form)
    print(request.form['user'])
    print(request.form.get('user'))
    print(request.form.getlist('user'))
    print(request.form.get('nickname', default='little apple'))
  return json5.dumps({
    'code': '0'
  })


if  __name__  ==  '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
