#!/bin/bash

# presently we only have set the dev build
BUILD=development
PROJECT=boxing
PROJECT_ROOT=/var/www/boxing-api

# log this build
echo $(date +"%d_%m_%Y_%H_%M_%S") >> logs/initialize.log

# delete default nginx config
rm /etc/nginx/sites-enabled/default

# set ngninx configurations
cp build/nginx/$BUILD/$PROJECT /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/$PROJECT /etc/nginx/sites-enabled/$PROJECT

# set settings file
ln -s $PROJECT_ROOT/build/django/$BUILD/settings.py $PROJECT_ROOT/boxing/settings.py

# initialize Django project
python3 $PROJECT_ROOT/manage.py collectstatic --noinput
python3 $PROJECT_ROOT/manage.py makemigrations --noinput
python3 $PROJECT_ROOT/manage.py migrate --noinput

# create superuser
