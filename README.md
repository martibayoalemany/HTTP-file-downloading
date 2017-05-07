
`python-file-downloader` 
File downloader in python as required for a coding entry test to a company

## Initialize project (python 2.x)
```
virtualenv ~/.virtualenvs/venv27 
source ~/.virtualenvs/venv27/bin/activate
pip install -r requirements.txt
cd src
python setup.py test
```

## Initialize project (python 3.x)
```
python3 -m venv .venv3 
source ~/.virtualenvs/.venv3/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd src
python setup.py test
```

## Documentation
Install and execute Sphinx

```
pip install Sphinx
make html
```