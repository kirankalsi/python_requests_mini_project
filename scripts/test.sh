#! /bin/bash

sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv proj_venv
. proj_venv/bin/activate
pip3 install -r service1/requirements.txt

pytest ./service1 --cov ./service1/application
pytest ./service2 --cov ./service2/application

deactivate
rm -rf proj_venv