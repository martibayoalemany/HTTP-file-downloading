### python-file-downloader

Checking the file downloading apis

### Remarks
 * BeautifulSoup and mechanize only works with python 2.7

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

### Using the normal requests api to download images (python 2.x)
Download with 2 processes and 100 links took 9.73853898048, failed 0 
Download with 4 processes and 100 links took 4.33651399612, failed 0 
Download with 8 processes and 100 links took 2.54078197479, failed 0