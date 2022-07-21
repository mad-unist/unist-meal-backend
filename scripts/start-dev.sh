#!/bin/bash

# Install dependencies
poetry install --no-interaction --no-ansi;

# Make sure that we're in the correct path to run server
cd src

# Run server
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000