# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
import codecs
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
LOGISITICAL_PATH = os.path.join(path_home, "LOGISTICAL.csv")
NEWS_PATH = os.path.join(path_home, "NEWS.csv")
DONATION_PATH = os.path.join(path_home, "DONATION.csv")
FACTORY_PATH = os.path.join(path_home, "FACTORY.csv")
CLINIC_PATH = os.path.join(path_home, "CLINIC.csv")


"""
Tools
"""
def csv_helper(fpath, headers):
    result = []
    with codecs.open(fpath, encoding='utf-8') as f:
        for line in f.readlines()[1:]:
            csv_data = line.strip().split(",")
            result.append(dict(zip(headers,csv_data)))
    return result

def filter_entity(entity_list, search_fields, keywords):
    recall_set = []
    for entity in entity_list:
        if is_valid_entity(entity, search_fields, keywords):
            recall_set.append(entity)
    return recall_set

def is_valid_entity(entity, search_fields, keywords):
    field_values = []
    for search_field in search_fields:
        if search_field in entity:
            field_values.append(entity[search_field])
    field_val_concat = ' '.join(field_values).lower()
    is_valid = True
    for keyword in keywords.split(' '):
        try:
            if keyword.lower() not in field_val_concat:
                is_valid = False
                break
        except Exception as ex:
            is_valid = False
    return is_valid

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
        resp_data = csv_helper(HOSPITAL_PATH,HOSPICAL_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/hospital_search')
def hospital_search():
    keyword = request.args.get('keyword')
    print('keyword: %s' % keyword)
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        hospital_all = csv_helper(HOSPITAL_PATH,HOSPICAL_HEADERS)
        search_fields = ['hospital_name', 'hospital_addr', 'hospital_requirement']
        print('search_fields created: %s' % search_fields)
        search_result = filter_entity(hospital_all, search_fields, keyword)
        resp['success'] = True
        resp['data'] = search_result
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
        resp_data = csv_helper(LOGISITICAL_PATH,LOGISTICS_HEADERS )
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
        resp_data = csv_helper(CLINIC_PATH,CLINIC_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
