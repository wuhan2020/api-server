# -*- coding: utf-8 -*-
from flask import Blueprint
import csv
import os 

data = Blueprint('register', __name__)
from index import *
PATH_HOSPITAL = os.path.join(path_home, "HOSPITAL.csv")
PATH_LOGISTICAL = os.path.join(path_home, "LOGISTICAL.csv")

@data.before_request
def before(*args,**kwargs):
    pass

@data.route('/index')
def index():
    return "hello world"



@data.route('/logistical_list')
def logistical_list():
    try:
        logisticals = []
        with open(PATH_LOGISTICAL) as f:
            for line in f.readlines():
                logistical = line.strip().split(",")
                item = {}
                item["name"] = logistical[0]
                item["area"] = logistical[1]
                item["ability"] = logistical[2]
                item["url"] = logistical[3]
                item["phone"] = logistical[4]
                logisticals.append(item)
        response = {
            "success" : True,
            "data" : logisticals,
        }
    except Exception as e:
        response = {
            "success" : False,
            "message" : e.message, 
        }
    return json.dumps(response,ensure_ascii=False)

@data.route('/hospital_list')
def hospital_list():
    try:
        data = csv.reader(open(PATH_HOSPITAL, 'r'))
        next(data)
        hospitals = []
        for hospital in data:
            item = {}
            item["province"] = hospital[0]
            item["name"] = hospital[1]
            item["address"] = hospital[2]
            item["people"] = hospital[3]
            item["need"] = hospital[4]
            item["link"] = hospital[5]
            item["phone"] = hospital[6]
            item["extra"] = hospital[7]
            hospitals.append(item)
        response = {
            "success" : True,
            "data": hospitals,
        }
    except Exception as e:
        response = {
            "success":False,
            "msg":e.message,
        }
    return json.dumps(response,ensure_ascii=False)

