# wuhan2020-api-server
武汉新型冠状病毒防疫信息收集平台后端

## 快速上手
``` bash
git clone https://github.com/wuhan2020/api-server
cd api-server
git clone https://github.com/wuhan2020/wuhan2020
pip install -r requirements.txt
bash bootstrap
```

然后就可以在`http://your-ip:9000/wuhan2020/`调试api
注意`list_path`是在`utils.py`中被`data.route`注册的path,
`your-ip`默认是127.0.0.1

## Docker 容器运行
需要安装[Docker客户端](https://www.docker.com/products/docker-desktop).

### Build Docker Image
在本项目根目录下执行 `docker build -t api-server:default .`. 
注意国内这一步可能会耗时较长.

### Run Docker Image
执行 `docker run --name api-server --publish 5000:5000 api-server:default ` 后可在本地浏览器中打开http://localhost:5000/wuhan2020/{endpoint}. (使用 `-d` 进入detach模式)

_如果出现 `The container name "/api-server" is already in use` 报错可先执行 `docker rm api-server` 删除残留的同名容器._

### Stop Docker Container
执行 `docker stop api-server `停止运行中的容器.

## 项目文件说明

```
.
├── bootstrap(阿里云serverless启动脚本)
├── index.py(flask应用默认配置脚本)
└── utils.py(flask蓝图功能)
```
**index.py**说明
```python
# -*- coding: utf-8 -*-
from flask import  Flask,session,request,Blueprint
import os
import sys
import json
import platform
import datetime
from utils import data

app = Flask(__name__)
app.debug = True
# 默认开启debug
path_prefix= "/wuhan2020"
# url请求前缀，默认要加/wuhan2020
if platform.system()=="Linux":
    path_home="/home/wuhan2020/wuhan2020"
else:
    path_home=os.path.join(app.root_path,"wuhan2020")
# 阿里云serverless使用挂载nas远程目录来存放缓存文件
# 在本机调试时，缓存文件夹将存放在项目根目录
if not os.path.exists(path_home):
    os.mkdir(path_home)
app.register_blueprint(data, url_prefix=path_prefix)
#使用flask蓝图功能来注册http-router

if __name__ == '__main__':
    # 使用aliyun默认端口9000
    port = os.environ.get("FC_SERVER_PORT", "9000")
    app.run(host='127.0.0.1', port=int(port))
```
## 前端项目issues
https://github.com/wuhan2020/front-pages/issues
