FROM timestamp_bitcoind_base:latest
MAINTAINER Liyi Zhou <lzhou1110@gmail.com>

# Move configuration files
ADD Bitcoin.conf $HOME/.bitcoin/

# Move modification files
ADD bitcoin_modification /bitcoin_modification

# Removing seed nodes
RUN rm bitcoin/contrib/seeds/nodes_main.txt
RUN rm bitcoin/contrib/seeds/nodes_test.txt

# Replace all modified files
RUN yes | cp -rf bitcoin_modification/* bitcoin

WORKDIR /bitcoin

RUN ./configure --without-gui --without-miniupnpc --disable-hardening --enable-debug

# Build with 12 processes
RUN make -j 12