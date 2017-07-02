#!/usr/bin/env bash
SCRIPT_DIR=$(realpath $(dirname $0))
ROOT_DIR=${SCRIPT_DIR}/..
SRC_DIR=${ROOT_DIR}/src

echo ${ROOT_DIR}
cd ${ROOT_DIR}

source ${SCRIPT_DIR}/activate

if ! which python3 > /dev/null; then
   sudo apt install python3 -y
fi

if ! which pip > /dev/null; then
   sudo apt install python-pip -y
fi


# python 3
python3 -m venv .venv3 
source .venv3/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# python 2.7
virtualenv .venv27
source .venv27/bin/activate
pip install --upgrade pip

python setup.py test
