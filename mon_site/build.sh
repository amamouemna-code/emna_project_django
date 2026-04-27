#!/usr/bin/env bash
set -o errexit

# Cette ligne installe Django et Gunicorn sur Render
pip install -r requirements.txt 

python manage.py collectstatic --no-input
python manage.py migrate