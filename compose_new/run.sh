#!/usr/bin/env bash
docker container prune
docker-compose down
docker-compose up -d --scale pyattacker=200
