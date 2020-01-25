# -*- coding: utf-8 -*-
from flask import  Flask,session,request,Blueprint
import os
import sys
import json
import platform
import datetime
from utils import data

app = Flask(__name__)
app.debug = True
path_prefix= "/wuhan2020"
if platform.system()=="Linux":
    path_home="/home/wuhan2020/wuhan2020"
else:
    path_home=os.path.join(app.root_path,"wuhan2020")
if not os.path.exists(path_home):
    os.mkdir(path_home)
app.register_blueprint(data, url_prefix=path_prefix)

@app.route('/')
def index():
    response={"1":"2"}
    return json.dumps(response,ensure_ascii=False)

if __name__ == '__main__':
    port = os.environ.get("FC_SERVER_PORT", "9000")
    app.run(host='0.0.0.0', port=int(port))
