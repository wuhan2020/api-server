# API Server

![Python3.6](https://img.shields.io/badge/python-3.6-green.svg?style=flat-square&logo=python&colorB=blue)
[![Slack Channel](https://img.shields.io/badge/Slack%20Channel-%23api--server-green.svg?style=flat-square&colorB=blue)](https://app.slack.com/client/TT5U1VCPQ/CT3V5CDKJ)
[![Built with love](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square)](https://img.shields.io/badge/BUILT%20WITH-LOVE-orange?style=flat-square&logo=love)

[中文文档](README.md)

This a backend API service of the voluntary information collection and sharing platform to fight against the 2019-nCoV outbreak in Wuhan and the world. 

The API is designed to be thin and stateless. It relies on the data collected and validated by other sub-projects, transform and expose them through standard RESTful APIs. The service is written in Python and Flask.

## Quick Start

## Development

### Running locally with Docker

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
and then open `http://localhost:9000/wuhan2020/{endpoint}` in your browser. _(Add `-d` to run the Docker container in detach/background mode)_

_If you ran into error `The container name "/api-server" is already in use`, please run `docker rm api-server` to delete previous container which has the same name._

#### Stop running Docker container

Run:
```
docker stop api-server 
```
to stop the running container.

## Deployment

## Contributing

Please see [Conntributing Guide](CONTRIBUTING.md)

## Front-end issues

Plases check [here](https://github.com/wuhan2020/front-pages/issues)
