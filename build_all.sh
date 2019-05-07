#!/usr/bin/env bash
./build_bitcoind_base.sh
./build_bitcoind_original.sh
./build_bitcoind_with_peers.sh
./build_attacker.sh