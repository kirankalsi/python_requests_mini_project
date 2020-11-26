#! /bin/bash

pytest ./service1 --cov ./service1/application
pytest ./service2 --cov ./service2/application