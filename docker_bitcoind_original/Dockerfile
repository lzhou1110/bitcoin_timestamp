FROM timestamp_bitcoind_base:latest
MAINTAINER Liyi Zhou <lzhou1110@gmail.com>

WORKDIR /bitcoin

RUN ./configure --without-gui --disable-wallet --without-miniupnpc --disable-hardening --enable-debug

# Build with 12 processes
RUN make -j 12