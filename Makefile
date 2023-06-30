.PHONY: deps test

deps:
	pip install -r requirements.txt; \
		pip install -r test_requirements.txt
lint:
	flake8 hello_world test
test:
	python py.test
run:
	python main.py
