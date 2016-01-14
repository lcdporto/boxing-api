# Boxing Api #

## Using the Docker Image for Development ##

* You need to install docker

$ docker pull lcdporto/boxing-api
$ docker run -tid --name boxing-api -p 80:80 lcdporto/boxing-api

* By default assumes development settings
* In development mode a pre-populated database is used
* User email is admin@lcdporto.org and password is admin
