### python-file-downloader

Checking the file downloading apis

### Builds or installs the package
```
# SDIST - Generates egg-info and dist/*.tar.gz , sdist uses distutils and setuptools
python setup.py sdist

# Generates egg-info, dist/*.py2-none-any.whl and build 
python setup.py bdist_wheel

# Editable through a local link
pip install -e .

# Copies the file into the .venv3
pip install .
```

### Uploads the package - first try
Creates  ~/.pypirc
```
[pypi]
repository=https://pypi.python.org/pypi
username=<username>
password=<password>
```
distutils checks the schema (http or https) using the section name,
the next command fails locally.
```
python setup.py sdist upload -r pypi
```

### Uploads the package - second try

```
[https://pypi.python.org/pypi]
repository=https://pypi.python.org/pypi
username=<username>
password=<password>
```
```
python setup.py sdist upload -r https://pypi.python.org/pypi
```
Upload failed (401): You must be identified to edit package information
error: Upload failed (401): You must be identified to edit package information

### Uploads the package (twine) - third try
```
python setup.py sdist bdist_wheel
pip install twine
ls dist | xargs -n1 twine register
twine upload dist/*
```
## Initialize coding environment (python 2.x)
```
virtualenv ~/.virtualenvs/venv27 
source ~/.virtualenvs/venv27/bin/activate
pip install -r requirements.txt
cd src
python setup.py test
```

## Initialize coding environment (python 3.x)
```
python3 -m venv .venv3 
source .venv3/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd src
python setup.py test
```
## Add a new dependency
It installs and adds a dependency to requirements.txt
It prevents adding the dependencies of the dependencies, so if 
a module changes we don't need to carry on with outdated dependencies.
```
source scripts/activate
pip_ins_free coverage
```
## Testing with tox
```
 tox 
 tox --recreate -e py27
```


## TODO's 
* Setup a local web server for network independent testing
