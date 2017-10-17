# Pyramid_bugsnag

[![CircleCI](https://circleci.com/gh/pior/pyramid_bugsnag.svg?style=svg)](https://circleci.com/gh/pior/pyramid_bugsnag)
[![PyPI](https://img.shields.io/pypi/v/pyramid-bugsnag.svg)](https://pypi.python.org/pypi/pyramid-bugsnag)


## Installing


```shell
$ pip install pyramid_bugsnag
```


## Usage

In your paster config:

```ini
[app:main]
pyramid.includes = pyramid_bugsnag

# Mandatory
bugsnag.api_key = ba10ba10ba10ba10ba10ba10ba10ba10

# All string and boolean options are supported:
bugsnag.release_stage = production
bugsnag.send_code = true
```

Full list of options on [docs.bugsnag.com](https://docs.bugsnag.com/platforms/python/other/configuration-options/)


## Development

Development dependencies are managed by [Pipenv](https://docs.pipenv.org/)

Install Pipenv:
```shell
$ pip install pipenv
```

Create/update your development environment:
```shell
$ pipenv install --dev
...

$ pipenv shell
(new shell)

$
```

Run the tests:
```shell
$ pytest -v
```

Run the linters:
```shell
$ pylama
```
