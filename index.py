# -*- coding: utf-8 -*-
from flask import  Flask
from utils import data

app = Flask(__name__)
app.debug = True
path_prefix= "/wuhan2020"
# url请求前缀，在http路径中要加/wuhan2020/
app.register_blueprint(data, url_prefix=path_prefix)
#使用flask蓝图功能来注册http-router


def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == '__main__':
    app.run()
