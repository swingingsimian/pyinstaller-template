# pyinstaller_template
Simple example of pyinstaller usage including package directory and exe build.

https://pyinstaller.readthedocs.io/en/stable/usage.html


## Setup
To develop and run the pyinstaller_template directly from the repository directory:

####Pre-requisites
```
python
pyenv
```


#### Python Set Up
```
PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install -v 3.4.3
pyenv local 3.7.6  
export PIPENV_PYTHON=~/.pyenv/shims/python
make install
```

Note: `--enable-framework` is required for pyinstaller to find ibpython3.4.dylib during build of the executable.

To make the executable:

```
make executable
```

## Running
The pyinstaller-template can be run as a python module:

```
usage: [pipenv run] python -m pyinstaller_template [-h] --name NAME [--verbose]

optional arguments:
  -h, --help     show this help message and exit
  --name NAME    The name of the person you wish to say hello to (default: None)
  --verbose, -v  Increase output verbosity (default: False)

```
Or directly as an executable after `make executable`:



## Development

### Set Up Developer Tools

```
make install-dev
```

### Installing a Package

```
pipenv install [--dev] package_name
```

### Testing

Tests and associated data are located in:

```
tests/
```

To run the tests:

```
make test     # Runs tests using local pipenv
```

Or to pass parameters to pytest specify PYT_PARAMS e.g. running a single test:

```
make test PYT_PARAMS='tests.test_pyinstaller_template.py::test_name -svv'
```



