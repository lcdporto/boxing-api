# use this as the base image
FROM ubuntu:14.04

# maintainer information
MAINTAINER Ricardo Lobo <ricardolobo@audienciazero.org>

# by default we are in development mode
# this is set with app_in_production env var
ENV APP_IN_PRODUCTION=false
ENV SECRET_KEY=alwayskeepyourkeysecret

# install packages
RUN apt-get update && \
apt-get -y install \
python3-pip \
python3-dev \
nginx \
supervisor \
wget \
sqlite3

# install pillow dependencies, pillow is
# required by django's imagefield
# following official basic installation
# http://pillow.readthedocs.org/en/3.0.x/installation.html#basic-installation
RUN apt-get -y install \
libtiff5-dev \
libjpeg8-dev \
zlib1g-dev \
libfreetype6-dev \
liblcms2-dev \
libwebp-dev \
tcl8.6-dev \
tk8.6-dev \
python-tk

# copy django project
ADD . /var/www/boxing-api
WORKDIR /var/www/boxing-api

# install python dependencies using pip3
RUN pip3 install -r requirements.txt

# set locale to european portuguese
RUN locale-gen pt_PT.UTF-8

# make initialize script executable
RUN chmod ug+x /var/www/boxing-api/initialize.sh

# supervisor configuration
COPY dist/common/supervisor/boxing.conf /etc/supervisor/conf.d/boxing.conf
CMD ["/usr/bin/supervisord"]