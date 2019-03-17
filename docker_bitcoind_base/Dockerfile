FROM ubuntu:18.04
MAINTAINER Liyi Zhou <lzhou1110@gmail.com>

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get update
RUN apt-get install -y build-essential libtool autotools-dev automake pkg-config bsdmainutils python3
RUN apt-get install -y libssl-dev libevent-dev libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-test-dev libboost-thread-dev
RUN apt-get install -y libzmq3-dev
RUN apt-get install -y wget
RUN apt-get install -y libdb4.8-dev libdb4.8++-dev
RUN apt-get install -y git
RUN apt-get install -y curl

WORKDIR /
RUN git clone https://github.com/wolfcw/libfaketime.git
WORKDIR /libfaketime/src
RUN make install

WORKDIR /
ADD bitcoin /bitcoin
# Install db4.sh
RUN ./bitcoin/contrib/install_db4.sh `pwd`
# Generating keys
RUN ./bitcoin/autogen.sh