#!/bin/bash

# Make sure that we're in the correct path to run server
cd src

# Run server
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:8000 --threads 2 --max-requests 10000 config.wsgi