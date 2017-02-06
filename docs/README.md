
`george_rowberry_python` is a snippet of python code to download pictures.  
It is developed for an entry test requirement for a company.

## Installation

The development environment was linux and the code targets `python2.7`  
To install the dependencies you will need to setup a virtual environment using the following command.

``` sh
virtualenv .venv // for python 2.7
python3 -m venv .venv // for python 3.5
```

## Usage

**Syntax:** download **(** [`-f filename`] **)**

### Arguments

* `filename` *String* (optional)
A text file containing a list of urls to images

### To-dos:
- use hyper for http2.0 support  
` from hyper import HTTPConnection `