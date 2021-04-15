from flask import Flask  
from flask import request
from flask import redirect
from flask import jsonify
import json5

from api.sendemail import sendEM
from api.senddingding import send_ding

app = Flask(__name__)
@app.route('/sendemail', methods=['GET','POST'])

def sendemail():
    op=request.json.get('op')
    subject=request.json.get('subject')
    content=request.json.get('content')
    s=sendEM()
    s.sendmsg(op,subject,content)
    return json5.dumps({
    'code': '0'
  })

@app.route('/senddingding', methods=['GET','POST'])

def senddingding():
    op=request.json.get('op')
    content=request.json.get('content')
    send_ding(op,content,"监控")
    
    return json5.dumps({
    'code': '0'
  })

if  __name__  ==  '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
