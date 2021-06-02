PROJECT_NAME=news-crawler-api

.virtualenv:
	virtualenv -p python3 .virtualenv
	. .virtualenv/bin/activate; \
	pip install -r requirements.txt

clean:
	rm -rf *.egg-info
	rm -rf .virtualenv/

test: .virtualenv
	(. .virtualenv/bin/activate; \
	pycodestyle --max-line-length=79 api test; \
	pylint --fail-under=9.0 --rcfile=pylintrc api; \
	pylint --fail-under=9.0 --rcfile=pylintrc-test test; \
	nosetests test --with-coverage --cover-tests --cover-min-percentage=60 --cover-package=api)

build: test clean

.PHONY: test clean build
