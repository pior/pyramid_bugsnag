# Pyramid_bugsnag

[![Build](https://travis-ci.org/pior/pyramid_bugsnag.svg?branch=multi-python-ci-travis)](https://travis-ci.org/pior/pyramid_bugsnag)
[![PyPI](https://img.shields.io/pypi/v/pyramid-bugsnag.svg)](https://pypi.python.org/pypi/pyramid-bugsnag)


## Installing


```shell
$ pip install pyramid_bugsnag
```


## Usage

Include *pyramid_bugsnag* either in your paster config:

```ini
[app:main]
pyramid.includes = pyramid_bugsnag
```

or on your Pyramid configurator:

```python
config = Configurator()
config.include('pyramid_bugsnag')
```

The *Bugsnag* client can be configured through the Paster settings:

```ini
bugsnag.api_key = ba10ba10ba10ba10ba10ba10ba10ba10

# All string and boolean options are supported:
bugsnag.release_stage = production
bugsnag.send_code = true
```

But nothing stops you from configuring the client directly:

```python
bugsnag.configure(api_key='ba10ba10ba10ba10ba10ba10ba10ba10')
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
