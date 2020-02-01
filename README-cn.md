# API Server

![Python3.6](https://img.shields.io/badge/python-3.6-green.svg?style=flat-square&logo=python&colorB=blue)
[![Slack Channel](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)
[![Built with love](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square)](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square&logo=love)
![Build Status](https://github.com/wuhan2020/api-server/workflows/Tests%20on%20Pull%20Requests%20and%20Master/badge.svg?branch=master&event=push)

[English Version](README.md)

这是一个为了抗击在武汉乃至全球爆发的新型冠状病毒而建设的志愿信息收集和分享平台的后端API服务。

此API使用Python 和 Flask 编写，意在轻量化和无状态，通过标准的RESTFul接口传输依靠从其他子项目收集并验证的数据。

## 快速上手

克隆此仓库及子模块仓库：
```
git clone https://github.com/wuhan2020/api-server
cd api-server
git clone https://github.com/wuhan2020/wuhan2020
```

### 在本地 Docker 容器运行（推荐）

首先，你需要安装[Docker客户端](https://www.docker.com/products/docker-desktop).

#### 构建 Docker 镜像 

在克隆的本仓库根目录下运行:
```
docker build -t api-server:default .
```
* 注意：这一步耗时取决于所在国家或地区

#### 运行已构建的 Docker 镜像

运行：
```
docker run --name api-server --publish 9000:9000 api-server:default 
```
然后在浏览器中打开 `http://localhost:9000`  。(使用 `-d` 来以后台模式（Detached mode）运行 Docker 容器)

在这一步后你应该可以看到记录了可用的端点的Swagger页面。

如果出现 `The container name "/api-server" is already in use` 报错可先执行 `docker rm api-server` 删除残留的同名容器.

#### 停止运行中的 Docker 容器

运行：
```
docker stop api-server 
```
停止运行中的容器.

### 在Python环境中运行

确保你已经安装 **Python3.6**  (一般来讲你应该会使用 [VirtualEnv](https://docs.python.org/3.6/tutorial/venv.html)
或是 [PyEnv](https://github.com/pyenv/pyenv)). 然后在克隆仓库的根目录运行：

```
pip install -U -r requirements.txt
```

启动服务器:

```
bash bootstrap
```
在浏览器中打开`http://localhost:9000`，你应该可以看到记录了可用的端点的Swagger页面。.


## 开发

待更新...

## 部署
待更新...

## 贡献

参照[贡献指南](CONTRIBUTING.md)

## 前端issues

请查阅[这里](https://github.com/wuhan2020/front-pages/issues)
