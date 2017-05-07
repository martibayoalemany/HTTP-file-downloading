
### python-file-downloader

File downloader in python as required for a coding entry test to a company

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
source ~/.virtualenvs/.venv3/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd src
python setup.py test
```

### Using the normal requests api to download images (python 2.x)

Download with 2 processes and 100 links took 9.73853898048, failed 0 
 
Download with 4 processes and 100 links took 4.33651399612, failed 0 
 
Download with 8 processes and 100 links took 2.54078197479, failed 0 
 
