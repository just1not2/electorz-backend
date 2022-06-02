# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# Mozilla Public License Version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)

PYTHON_BINARY=/usr/bin/python3

default: start

.env:
	cp .env.template .env

.PHONY: install
install:
	${PYTHON_BINARY} -m pip install -r requirements/common.txt
	${PYTHON_BINARY} -m pip install -r requirements/dev.txt

.PHONY: lint
lint:
	pylint .

.PHONY: stack
stack:
	docker-compose up -d

.PHONY: start
start:
	python3 app.py
