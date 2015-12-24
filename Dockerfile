# Use this as a base image
FROM ubuntu:14.04

# Maintainer Info
MAINTAINER Ricardo Lobo <ricardolobo@audienciazero.org>

# by default we are in development
# set env var app_in_production to false
ENV APP_IN_PRODUCTION=false

# install packages
RUN apt-get update && \
apt-get -y install \
python3-pip \
python3-dev \
nginx \
supervisor \
wget \
sqlite3

# Configure Django project
ADD . /var/www/boxing-api
WORKDIR /var/www/boxing-api

# Install Dependencies Using Pip
RUN pip3 install -r requirements.txt

# Locale
RUN locale-gen pt_PT.UTF-8

# run initialize script
RUN chmod ug+x /var/www/boxing-api/initialize.sh

# supervisor configuration
COPY dist/development/supervisor/boxing.conf /etc/supervisor/conf.d/boxing.conf
CMD ["/usr/bin/supervisord"]