#!/bin/bash

coverage run --source='campusZen' manage.py test ./campusZen/tests/

coverage html

xdg-open htmlcov/index.html || open htmlcov/index.html || start htmlcov/index.html

