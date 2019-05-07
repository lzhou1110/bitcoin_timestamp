#!/usr/bin/env bash
docker container prune
docker-compose down
./build_bitcoind_base.sh
./build_bitcoind_original.sh
./build_attacker.sh
#docker-compose up -d