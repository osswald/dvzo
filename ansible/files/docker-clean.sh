#!/bin/bash

docker stop $(docker ps -q)
docker system prune -a
docker system prune --volumes
