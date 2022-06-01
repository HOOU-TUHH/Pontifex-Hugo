#!/bin/bash

docker run -it --rm -v `pwd`:/app -w /app node:17-bullseye npm install
docker run -it --rm -v `pwd`:/app -w /app node:17-bullseye npm run build
docker run -it --rm --name apache-server -p 8080:80 -v `pwd`/public:/usr/local/apache2/htdocs/ httpd:2.4-alpine

