.PHONY: help init clean test clean-build isort run

.DEFAULT: help

help:
	@echo "make init"
	@echo "		  Innstall dependencies"
	@echo "make clean"
	@echo "       Prepare development environment, use only once"
	@echo "make clean-build"
	@echo "       Clear all build directories"
	@echo "make isort"
	@echo "       Run isort command cli in development features"
	@echo "make lint"
	@echo "       Run lint"
	@echo "make test"
	@echo "       Run tests"
	@echo "make run"
	@echo "       Run the application"

init:
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pyc|.DS_Store$$" | xargs rm -rf

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint: clean
	pylint infertype

test: lint
	pytest --verbose --color=yes $(TEST_PATH)

run: test
	python infertype/app.py
