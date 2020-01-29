import os
import yaml
import xmltodict
import json
import functools
import logging
from flask import abort
from flask_httpauth import HTTPTokenAuth

from config.settings import DEBUG_FLAG

# TODO: use .gitignore hide token; i don't know how to use this auth in blueprint
auth = HTTPTokenAuth(scheme='Bearer')
test_token = 'test-safe-wuhan'
auth_file = os.path.join(os.path.abspath(__file__), 'auth/auth_info.json')
auth_token = test_token if DEBUG_FLAG else json.load(auth_file)['token']


@auth.verify_token
def auth_token_wrapper(token):
    if token == auth_token:
        return True
    return False


def csv_helper(fpath, headers):
    header_st = 2
    result = []
    with open(fpath) as f:
        for line in f.readlines()[2:]:
            csv_data = line.strip().split(",")
            result.append(dict(zip(headers, csv_data)))
    return result


def csv_with_medical_supplier(fpath, headers):
    header_st, spliter = 5, '#'
    result, total_header = [], []
    for h in headers:
        if isinstance(h, list):
            for sub_h in h:
                total_header.append(spliter.join(sub_h))
        else:
            total_header.append(h)
    with open(fpath) as f:
        for line in f.readlines()[header_st:]:
            csv_data = line.strip().split(",")
            result.append(dict(zip(total_header, csv_data)))
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
