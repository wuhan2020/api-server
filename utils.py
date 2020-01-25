# -*- coding: utf-8 -*-
from flask import Blueprint
import os
import json
import datetime
import platform
import csv
import os 

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

PATH_HOSPITAL = os.path.join(path_home, "HOSPITAL.csv")
PATH_LOGISTICAL = os.path.join(path_home, "LOGISTICAL.csv")
PATH_HOTEL = os.path.join(path_home, "HOTEL.csv")


@data.route('/hotel_list')
def hotel_list():
    try:
        hotels = []
        with open(PATH_HOTEL) as f:
            for line in f.readlines():
                hotel = line.strip().split(",")
                item = {}
                item["name"] = hotel[0]
                item["area"] = hotel[1]
                item["address"] = hotel[2]
                item["bed_nums"] = hotel[3]
                item["phone"] = hotel[4]
                hotels.append(item)
        response = {
            "success" : True,
            "data" : hotels,
        }
    except Exception as e:
        response = {
            "success" : False,
            "message" : e.message, 
        }
    return json.dumps(response,ensure_ascii=False)

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
            if len(hospital)!=8:
                continue
            item["province"]=hospital[0]
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
