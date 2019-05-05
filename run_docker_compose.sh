#!/usr/bin/env bash
docker container prune
docker-compose down
./build_bitcoind_base.sh
./build_bitcoind.sh
#./build_miner.sh
./build_attacker.sh
docker-compose up