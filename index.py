# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.wrappers import Response as ResponseBase
from utils import data
import os

app = Flask(__name__)
app.debug = True
path_prefix= "/wuhan2020"
# url请求前缀，在http路径中要加/wuhan2020/
app.register_blueprint(data, url_prefix=path_prefix)
# 使用flask蓝图功能来注册http-router

class Response(ResponseBase):
    default_mimetype = 'application/json'

def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == '__main__':
    # 使用aliyun默认端口9000
    port = os.environ.get("FC_SERVER_PORT", "9000")
    app.response_class = Response
    app.run(host='127.0.0.1', port=int(port))
