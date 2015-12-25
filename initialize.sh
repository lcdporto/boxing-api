#!/bin/bash

LOGFILE=logs/initialize.log
PROJECT=boxing
PROJECT_ROOT=/var/www/boxing-api

if [ "$APP_IN_PRODUCTION" = false ]; then
    BUILD=development
else
    BUILD=production
fi

# log this build
echo $(date +"%d_%m_%Y_%H_%M_%S") >> $LOGFILE

# delete default nginx config
rm /etc/nginx/sites-enabled/default

# set ngninx configurations
cp dist/$BUILD/nginx/$PROJECT /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/$PROJECT /etc/nginx/sites-enabled/$PROJECT

# set settings file
ln -s $PROJECT_ROOT/dist/$BUILD/django/settings.py $PROJECT_ROOT/boxing/settings.py

# if in development copy the pre-populated development database if not already present
if [ "$APP_IN_PRODUCTION" = false ]; then
    # the -n flag means no clobber, i.e do not replace an existing file
    cp -n dist/$BUILD/database/boxing.sqlite3 $PROJECT_ROOT/

# collect static files (e.g. images to the static folder as defined in the settings)
python3 $PROJECT_ROOT/manage.py collectstatic --noinput
# apply migrations to the database
python3 $PROJECT_ROOT/manage.py migrate --noinput

exit 0
