# -*- coding: utf-8 -*-
from flask import Blueprint
import os
import json
import datetime
import platform
import csv
import os
import traceback
import yaml

from const import *

data = Blueprint('register', __name__)
if platform.system()=="Linux":
    path_home="/home/wuhan2020/wuhan2020"
else:
    from index import app
    path_home=os.path.join(app.root_path,"wuhan2020")
# wuhan2020文件夹为https://github.com/wuhan2020/wuhan2020项目文件的本地clone
# 阿里云serverless使用挂载nas远程目录来存放缓存文件；在本机调试时，缓存文件夹将存放在项目根目录

if not os.path.exists(path_home):
    os.mkdir(path_home)
"""
CACHE PATH
"""
HOSPITAL_PATH = os.path.join(path_home, "HOSPITAL.csv")
HOTEL_PATH = os.path.join(path_home, "HOTEL.csv")
LOGISITICAL_PATH = os.path.join(path_home, "LOGISITICAL.csv")
NEWS_PATH = os.path.join(path_home, "NEWS.csv")
DONATION_PATH = os.path.join(path_home, "DONATION.csv")
FACTORY_PATH = os.path.join(path_home, "FACTORY.csv")
CLINIC_PATH = os.path.join(path_home, "CLINIC.csv")


"""
Tools
"""
def csv_helper(fpath, headers):
    result = []
    with open(fpath) as f:
        for line in f.readlines():
            csv_data = line.strip().split(",")
            result.append(dict(zip(headers,csv_data)))
    return result

def yaml_helper(fpath):
    result = []
    with open(fpath, 'r') as f:
        result = yaml.load(f)
    return result


@data.route('/hospital_list')
def hospital_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = yaml_helper(HOSPITAL_PATH)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/hotel_list')
def hotel_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(HOTEL_PATH, HOTEL_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)

@data.route('/logstics_list')
def logstics_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(LOGISITICAL_PATH, LOGISITICAL_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)



@data.route('/news_list')
def news_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(NEWS_PATH, NEWS_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/donation_list')
def donation_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(DONATION_PATH, DONATION_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/factory_list')
def factory_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(FACTORY_PATH, FACTORY_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/clinic_list')
def clinic_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(CLINIC_PATH, CLINC_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
