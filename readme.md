# Boxing Api #

## Using the Docker Image for Development ##

* You need to install docker, after that simply open a terminal and type

```
$ docker pull lcdporto/boxing-api
$ docker run -tid --name boxing-api -p 80:80 lcdporto/boxing-api
```

* You are now a proud owner of a development api located at http://127.0.0.1
* By default the container assumes development settings
* In development mode a pre-populated database is used
* In development mode you have a user with email admin@lcdporto.org and password admin
