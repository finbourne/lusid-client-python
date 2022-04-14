#!/bin/bash -e

docker run --rm -it --name='tinyproxy' -p 8888:8888 --env BASIC_AUTH_USER=user --env BASIC_AUTH_PASSWORD=password monokal/tinyproxy:latest 'ANY'
#docker run --rm -it --name='tinyproxy' -p 8888:8888 monokal/tinyproxy:latest 'ANY'