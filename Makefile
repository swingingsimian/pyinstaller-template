.PHONY: help install install-dev clean format test
PKG_VERSION=$(shell pipenv run python setup.py --version)
PACKAGE_NAME=pyinstaller_template

default: help

help: ## List each of the make targets and the descriptive comment on its line
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/:[^#]*##/: /'

clean: ## Cleans make artefacts
	-pipenv --rm
	-rm -rf dist build *.egg-info *.exe.spec

format: ## Runs blacks and isort
	pipenv run black .
	pipenv run isort -rc .

install:  ## Installs dependencies using pipenv
	pipenv install '-e .'

install-dev: ## Installs dev dependencies using pipenv
	pipenv install --dev

test:  ## Run the pytests e.g. make test [ PYT_PARAMS='tests/test_interpolator.py::TEST_NAME]
	pipenv run pytest -svv ${PYT_PARAMS}

executable: install ## Builds executable for current OS
	pip install pyinstaller # Install to venv but not Pipfile

	-pipenv run pyinstaller --onefile  \
		--name ${PACKAGE_NAME}-${PKG_VERSION}.exe   \
		--paths $(shell pipenv --venv)/lib/python3.7/site-packages  \
		${PACKAGE_NAME}/__main__.py

    #--debug=imports
    #--name is used for build dir and exe file name
    #--hidden-import pkg_resources # This shouldn't be necessary as pkg_resources is seen in the warn log
    # However setuptools 45 seems to trigger this pkg_resources issue:
    # https://github.com/pyinstaller/pyinstaller/issues/4672
    # temp hack to get around the issue
    # pipenv install "setuptools<45.0.0"