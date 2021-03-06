#!/usr/bin/env make

init:
	pip install -r requirements.txt

setup:
	python subsync/model/train_data.py

train:
	python subsync/model/train_ann.py

eval:
	python subsync/model/eval_ann.py

logloss:
	python subsync/model/eval_logloss.py

convert:
	python subsync/model/convert.py

test:
	python subsync/model/test.py
.PHONY: test

freeze:
	pip freeze > requirements.txt

publish:
	python setup.py sdist upload -r pypi
