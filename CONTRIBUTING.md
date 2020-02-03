# Contributing Guide

## Structure

![Tech Arch Diagram](https://www.lucidchart.com/publicSegments/view/6ab27659-257a-44ce-a478-46dad3328b9c/image.png)

As the above Tech Arch diagram shows (dot-line entities mean they are not there yet), this project is purely data-driven and the core layout looks like the following:

```
src
├── __init__.py
├── api/
├── core/
├── main.py
├── swagger/
├── tests/
└── utils/
```

`main.py` is the entry point of the services and it helps:
- glue all sub API YML files together to an aggregated YML
- send the YML to connection which renders the Swagger UI and applies the API resolvers.
- load required service-level connfigurations (such as debug, logging, path to the data sources, etc.).

### To add new or edit on existing API endpoint(s)

In general you need to edit the `src/swagger/api.yml` and probably its dependencies (such as `donation.yml`). **Be aware that any changes to the YML files can change the data model and breaks the system and the API consumers.**

If you are using a local Python3.6 environment, setting `debug=True` in `main.py` will help you see the changes you made in the Swagger UI in real time. 

Be aware that the `operationId` field in the YML files works as automatic routers that map your endpoint to your Python views functions. To make the endpoints functional, you also have to add/edit the functions in `src/api`. The results of the functions need to be consistent with the data model defined in the API YML file(s).

## Development

![DevOps Pipeline](https://www.lucidchart.com/publicSegments/view/b853bf49-31fa-46ba-b732-2eb9de8a2cf8/image.png)

The above diagram shows how to work on this repo:

### Development Process

The development process of this project requires every contributor to fork the repo and only make PRs from the fork to `master` branch. 

#### Setup upstream

From within your fork, use:
```
git remote add upstream git@github.com:wuhan2020/api-server.git
```
to setup this repo as the `upstream`.

#### Keep up-to-date with the upstream

Everytime before you want to make new changes to the repo, use:
```
git fetch upstream
git rebase upstream/master
```
to update your fork with latest changes that have merged to `upstream`'s `master` branch.

#### Address comments
Once you have finished committing and pushing your changes to your remote fork, please create a PR from your remote repo following the PR template. One of the maintainers of the repo will review and merge your PR. Please note PR that fails the tests cannot be reviewed or merged.

## Deployment

The current deployment is under construction and subjects to change. New documentation is coming soon...
