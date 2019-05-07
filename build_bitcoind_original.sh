#!/usr/bin/env bash
docker build -f docker_bitcoind_original/Dockerfile -t lzhou1110/bitcoind_original:latest .
docker push lzhou1110/bitcoind_original
