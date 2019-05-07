#!/usr/bin/env bash
docker build -f docker_bitcoind_with_peers/Dockerfile -t lzhou1110/bitcoind_with_peers:latest -m 6g .
docker push lzhou1110/bitcoind_with_peers:latest