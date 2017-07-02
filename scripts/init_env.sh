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

pip install --upgrade pip

virtualenv .venv27
source .venv27/bin/activate

python3 -m venv .venv3 
source .venv3/bin/activate
pip install -r requirements.txt
python setup.py test
