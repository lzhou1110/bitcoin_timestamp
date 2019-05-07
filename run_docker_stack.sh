docker container prune
docker stack rm bitcoinstack
./build_bitcoind_base.sh
./build_bitcoind_original.sh
./build_attacker.sh
docker stack deploy -c docker-compose.yml bitcoinstack
