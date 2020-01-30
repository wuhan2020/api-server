# -*- coding: utf-8 -*-
from flask import Blueprint, request
from werkzeug.exceptions import *
import os
import json
import datetime
import platform
import csv
import os
import traceback
import yaml

import xmltodict

import json

from const import *

data = Blueprint('register', __name__)
if platform.system() == "Linux":
    path_home = "./wuhan2020"
else:
    from index import app
    path_home = os.path.join(app.root_path, "wuhan2020")
# wuhan2020文件夹为 https://github.com/wuhan2020/wuhan2020 项目文件的本地clone
# 阿里云serverless使用挂载nas远程目录来存放缓存文件；在本机调试时，缓存文件夹将存放在项目根目录

if not os.path.exists(path_home):
    os.mkdir(path_home)

"""
CACHE PATH
"""
HOSPITAL_PATH = os.path.join(path_home, "HOSPITAL.csv")
HOTEL_PATH = os.path.join(path_home, "HOTEL.csv")
LOGISTICS_PATH = os.path.join(path_home, "LOGISTICS.csv")
NEWS_PATH = os.path.join(path_home, "NEWS.csv")
DONATION_PATH = os.path.join(path_home, "DONATION.csv")
FACTORY_PATH = os.path.join(path_home, "FACTORY.csv")
CLINIC_PATH = os.path.join(path_home, "CLINIC.csv")


HOSPITAL_JSON = os.path.join(path_home, "HOSPITAL.json")
HOTEL_JSON = os.path.join(path_home, "HOTEL.json")
LOGISTICS_JSON = os.path.join(path_home, "LOGISTICS.json")
NEWS_JSON = os.path.join(path_home, "NEWS.json")
DONATION_JSON = os.path.join(path_home, "DONATION.json")
FACTORY_JSON = os.path.join(path_home, "FACTORY.json")
CLINIC_JSON = os.path.join(path_home, "CLINIC.json")

"""
Tools
"""


def csv_helper(fpath, headers):
    result = []
    with open(fpath) as f:
        for line in f.readlines()[1:]:
            csv_data = line.strip().split(",")
            result.append(dict(zip(headers, csv_data)))
    return result


def yaml_helper(fpath):
    result = []
    with open(fpath, 'r') as f:
        result = yaml.load(f)
    return result


def xml_helper(xml_path):
    with open(xml_path, 'r') as f:
        xml_str = f.read()
    json = xmltodict.parse(xml_str)
    return json


def json_helper(json_path):
    with open(json_path, 'r', encoding='UTF-8') as f:
        return json.loads(f.read())


@data.route('/json_test', methods=['GET'])
def json_test():
    path = os.path.join("/root/api-server/", "test.json")
    return json_helper(path)


@data.route('/xml_test', methods=['GET'])
def xml_test():
    path = os.path.join("/root/api-server/", "test.xml")
    return xml_helper(path)


@data.route('/hospital_list', methods=['GET'])
def hospital_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(HOSPITAL_PATH, HOTEL_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/hospitals', methods=['GET'])
def hospitals():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    code = 200
    try:
        hosptials_data = csv_helper(HOSPITAL_PATH, HOSPITAL_HEADERS)
        if 'limit' in request.args or 'skip' in request.args:
            skip = request.args.get('skip', type=int)
            limit = request.args.get('limit', type=int)
            hosptials_data_len = len(hosptials_data)
            if skip < 0 or limit < 0 or limit > 50:
                raise BadRequest('Bad input parameter.')
            if skip > hosptials_data_len:
                raise BadRequest("Index out of range.")
            if skip + limit > hosptials_data_len:
                limit = hosptials_data_len - skip
            resp['data'] = hosptials_data[skip:skip+limit]
        else:
            resp['data'] = hosptials_data
        resp['success'] = True
    except HTTPException as e:
        code = e.code
        resp['msg'] = str(e)
    except Exception as ex:
        code = 500
        resp['msg'] = str(ex)

    return json.dumps(resp, ensure_ascii=False), code


@data.route('/hotel_list', methods=['GET'])
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


@data.route('/logistics_list', methods=['GET'])
def logistics_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(LOGISTICS_PATH, LOGISTICS_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/news_list', methods=['GET'])
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


@data.route('/donation_list', methods=['GET'])
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


@data.route('/factory_list', methods=['GET'])
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


@data.route('/clinic_list', methods=['GET'])
def clinic_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(CLINIC_PATH, CLINIC_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/hospital_list_json', methods=['GET'])
def hospital_list_json():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = json_helper(HOSPITAL_JSON)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/hotel_list_json', methods=['GET'])
def hotel_list_json():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = json_helper(HOTEL_JSON)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/logistics_list_json', methods=['GET'])
def logistics_list_json():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = json_helper(LOGISTICS_JSON)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/news_list_json', methods=['GET'])
def news_list_json():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = json_helper(NEWS_JSON)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/donation_list_json', methods=['GET'])
def donation_list_json():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = json_helper(DONATION_JSON)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/factory_list_json', methods=['GET'])
def factory_list_json():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = json_helper(FACTORY_JSON)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/clinic_list_json', methods=['GET'])
def clinic_list_json():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = json_helper(CLINIC_JSON)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
