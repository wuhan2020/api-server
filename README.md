# API Server

![Python3.6](https://img.shields.io/badge/python-3.6-green.svg?style=flat-square&logo=python&colorB=blue)
[![Slack Channel](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)
[![Built with love](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square)](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square&logo=love)

[中文文档](README-cn.md)

This a backend API service of the voluntary information collection and sharing platform to fight against the 2019-nCoV outbreak in Wuhan and the world. 

The API is designed to be thin and stateless. It relies on the data collected and validated by other sub-projects, transform and expose them through standard RESTful APIs. The service is written in Python and Flask.

## Get Started

Please first clone this repository and the sub-module-repo by:

```
git clone https://github.com/wuhan2020/api-server
cd api-server
git clone https://github.com/wuhan2020/wuhan2020
```

### Running locally with Docker (Recommended)

**Pre-requisite: You have to have [Docker client](https://www.docker.com/products/docker-desktop) installed on your machine.**

#### Build the Docker image

Run:
```
docker build -t api-server:default .
```
from the root directory of the clone of this repo. Note this step could take a long time dependd on where you are located in.

#### Run built Docker image

Run:
```
docker run --name api-server --publish 9000:9000 api-server:default 
```
and then open `http://localhost:9000` in your browser. _(Add `-d` to run the Docker container in detach/background mode)_

You should see a Swagger page documents the available endpoints now.

_If you ran into error `The container name "/api-server" is already in use`, please run `docker rm api-server` to delete previous container which has the same name._

#### Stop running Docker container

Run:
```
docker stop api-server 
```
to stop the running container.

### Running with your own Python environment

Please make sure you have **Python3.6** installed, (ideally you should be using a [VirtualEnv](https://docs.python.org/3.6/tutorial/venv.html)
or something like [PyEnv](https://github.com/pyenv/pyenv)). Then from the root directory of the cloned repo, run:

```
pip install -U -r requirements.txt
```

and then start the server by:

```
bash bootstrap
```
now if you open `http://localhost:9000` in your browser, you should see a Swagger page documents the available endpoints.

## Development

Coming soon...

## Deployment

Coming soon...

## Contributing

Please see [Conntributing Guide](CONTRIBUTING.md)

## Front-end issues

Plases check [here](https://github.com/wuhan2020/front-pages/issues)
