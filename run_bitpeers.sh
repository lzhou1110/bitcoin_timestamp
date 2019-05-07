#!/usr/bin/env bash
docker build -f bitpeers/Dockerfile -t bitpeers:latest .
docker container stop bitpeers_container
docker container rm bitpeers_container
docker run --name=bitpeers_container bitpeers:latest
docker cp bitpeers_container:output.json peers_json_backup/output.json

