# 简体中文 | [English](./README_EN.md) 

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

随后便可在 `http://{your-ip}:9000/wuhan2020/{list_path}` 调试 api

注意 `list_path` 为 `utils.py` 中被 `@data.route()` 中注册的 `path`, `your-ip` 默认是 `127.0.0.1`.

## 在 Docker 容器运行
需要安装[Docker客户端](https://www.docker.com/products/docker-desktop).

### 制作 Docker 镜像
在本项目根目录下执行 `docker build -t api-server:default .`.

* 注意：国内这一步可能会耗时较长.

### 创建 Docker 容器
执行 `docker run --name api-server --publish 5000:5000 api-server:default ` 后可在本地浏览器中打开 http://localhost:5000/wuhan2020/{endpoint}. (使用 `-d` 进入detach模式)

_如果出现 `The container name "/api-server" is already in use` 报错可先执行 `docker rm api-server` 删除残留的同名容器._

### 停止 Docker 容器
执行 `docker stop api-server ` 停止运行中的容器.

## 项目文件说明

```
.
├── bootstrap (阿里云serverless启动脚本)
├── config (flask config dir)
├── swagger (swagger 暂时还不能用, 待适配.)
├── test (test 数据目录, 参照wuhan2020的[readme](https://github.com/wuhan2020/wuhan2020), 移除个人的联系方式和银行卡信息.)
├── wuhan2020 (submoudle, 用于获取data-sync同步过来的数据.)
├── index.py (flask应用默认配置脚本)
└── utils.py (flask蓝图, 目前有csv和json的接口, csv的加上了bearer token 认证, json的接口暂时不能用.)
```

## 配置说明

```
# Flask config
Config

# cache dir
CacheCfg
 - csv;
 - json;
```

## 测试

`dev url`是 `http://127.0.0.1:9000/wuhan2020/xxx_list`

```sh
# dev
curl --location --request GET '127.0.0.1:9000/wuhan2020/logistical_list' \
--header 'Authorization: Bearer test-safe-wuhan'
# product
curl --location --request GET '127.0.0.1:9000/wuhan2020/logistical_list' \
--header 'Authorization: Bearer product-token'
```

## 遗留问题

- [ ] 添加swagger适配;
- [ ] csv转换出来都是拍平的字段, 里面有部分中文转英文需要帮助转成合适的英文, 实在找不到用拼音替代.


## 前端项目issues
https://github.com/wuhan2020/WebApp/issues