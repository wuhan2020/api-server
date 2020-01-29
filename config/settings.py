import os, sys

DEBUG_FLAG = True


def get_cache_path():
    path_home = './'
    if DEBUG_FLAG:
        path_home = os.path.join(path_home, 'test/data/')
    else:
        path_home = os.path.join(path_home, 'wuhan2020/data/')
    # wuhan2020文件夹为https://github.com/wuhan2020/wuhan2020项目文件的本地clone
    # 阿里云serverless使用挂载nas远程目录来存放缓存文件；在本机调试时，缓存文件夹将存放在项目根目录
    if not os.path.exists(path_home):
        os.mkdirs(path_home)
    return path_home


class Config(object):
    DEBUG = DEBUG_FLAG
    # 使用aliyun默认端口9000
    ENV = {
        "FC_SERVER_PORT": 9000,
    }


class CacheCfg(Config):
    CACHE_DIR = get_cache_path()
    # csv
    CSV_CACHE = CACHE_DIR + 'csv/'
    HOSPITAL_PATH = os.path.join(CSV_CACHE, "HOSPITAL.csv")
    HOTEL_PATH = os.path.join(CSV_CACHE, "HOTEL.csv")
    LOGISITICAL_PATH = os.path.join(CSV_CACHE, "LOGISTICAL.csv")
    NEWS_PATH = os.path.join(CSV_CACHE, "NEWS.csv")
    DONATION_PATH = os.path.join(CSV_CACHE, "DONATION.csv")
    FACTORY_PATH = os.path.join(CSV_CACHE, "FACTORY.csv")
    CLINIC_PATH = os.path.join(CSV_CACHE, "CLINIC.csv")
    # json
    JSON_CACHE = CACHE_DIR + 'json/'
    JSON_HOSPITAL_PATH = os.path.join(JSON_CACHE, "HOSPITAL.json")
    JSON_HOTEL_PATH = os.path.join(JSON_CACHE, "HOTEL.json")
    JSON_LOGISITICAL_PATH = os.path.join(JSON_CACHE, "LOGISTICAL.json")
    JSON_NEWS_PATH = os.path.join(JSON_CACHE, "NEWS.json")
    JSON_DONATION_PATH = os.path.join(JSON_CACHE, "DONATION.json")
    JSON_FACTORY_PATH = os.path.join(JSON_CACHE, "FACTORY.json")
    JSON_CLINIC_PATH = os.path.join(JSON_CACHE, "CLINIC.json")
