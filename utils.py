# -*- coding: utf-8 -*-
from flask import Blueprint

data= Blueprint('register', __name__)
from index import *

@data.before_request
def before(*args,**kwargs):
    pass

@data.route('/index')
def timmer():
    response=[
        "hello world"
    ]
    return json.dumps(response,ensure_ascii=False)
