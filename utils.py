# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, request
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
from tools import *

data = Blueprint('register', __name__)


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
    code = 200
    try:
        hosptials_data = csv_with_medical_supplier(
            current_app.config['HOSPITAL_PATH'], HOSPITAL_HEADERS)
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
@auth.login_required
def hotel_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(current_app.config['HOTEL_PATH'], HOTEL_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/logistics_list', methods=['GET'])
@auth.login_required
def logistics_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_with_medical_supplier(
            current_app.config['LOGISITICAL_PATH'], LOGISTICS_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/news_list', methods=['GET'])
@auth.login_required
def news_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(current_app.config['NEWS_PATH'], NEWS_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/donation_list', methods=['GET'])
@auth.login_required
def donation_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(
            current_app.config['DONATION_PATH'], DONATION_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/factory_list', methods=['GET'])
@auth.login_required
def factory_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_with_medical_supplier(
            current_app.config['FACTORY_PATH'], FACTORY_HEADERS)
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)


@data.route('/clinic_list', methods=['GET'])
@auth.login_required
def clinic_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        resp_data = csv_helper(
            current_app.config['CLINIC_PATH'], CLINIC_HEADERS)
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
        resp_data = json_helper(current_app.config['JSON_HOSPITAL_PATH'])
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
        resp_data = json_helper(current_app.config['JSON_HOTEL_PATH'])
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
        resp_data = json_helper(current_app.config['JSON_LOGISITICAL_PATH'])
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
        resp_data = json_helper(current_app.config['JSON_NEWS_PATH'])
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
        resp_data = json_helper(current_app.config['JSON_DONATION_PATH'])
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
        resp_data = json_helper(current_app.config['JSON_FACTORY_PATH'])
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
        resp_data = json_helper(current_app.config['JSON_CLINIC_PATH'])
        resp['success'] = True
        resp['data'] = resp_data
    except Exception as e:
        resp['msg'] = str(e)
    return json.dumps(resp, ensure_ascii=False)
