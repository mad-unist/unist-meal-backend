#!/bin/bash

# poetry install
poetry install --no-interaction --no-ansi

# Make sure that we're in the correct path to run test
cd src

# Run test
python manage.py test --keepdb $1