#!/usr/bin/env bash
docker build -f docker_attacker/Dockerfile -t lzhou1110/timestamp_attacker:latest .
docker push lzhou1110/timestamp_attacker
