#!/usr/bin/env bash
# exit on error
set -o errexit

echo `ls`
echo `which poetry`
echo `which poetry`
echo '....................'

poetry install

python manage.py collectstatic --no-input
python manage.py migrate