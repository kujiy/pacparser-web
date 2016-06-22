#!/bin/bash

# Proxy setting
# (make sure to set $PROXY environment in your docker-compose.yml)
export http_proxy=$PROXY  && \
export https_proxy=$PROXY && \
export HTTP_PROXY=$PROXY  && \
export HTTPS_PROXY=$PROXY && \
export ftp_proxy=$PROXY
echo "Acquire::ftp::proxy \"$PROXY/\"; \n Acquire::http::proxy \"$PROXY\";  \n Acquire::https::proxy \"$PROXY\"; " >> /etc/apt/apt.conf.d/proxy.conf

# Install pacparser(Internet access is necessary)
mkdir /tmp-pac && cd /tmp-pac
git clone https://github.com/pacparser/pacparser.git
cd /tmp-pac/pacparser

make -C src pymod
export NO_INTERNET=1 && make -C src install-pymod
rm -rf /tmp-pac

# run http server
cd /app
/usr/bin/supervisord

# VIM install for debug
apt-get update && apt-get install -y vim
