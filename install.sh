#!/bin/bash

### install for pocketsphinx as used by nevermisscalling

########## install centos dependencies
sudo yum -y install gcc automake autoconf libtool bison
sudo yum -y install sources/swig-2.0.10-57.1.x86_64.rpm
sudo yum -y python-devel

########## install sphinxbase
tar -xzvf sources/sphinxbase-5prealpha.tar.gz

cd sphinxbase-5prealpha
./autogen.sh
./configure
make
make install

cd ..

########## install pocketsphinx
tar -xzvf sources/pocketsphinx-5prealpha.tar.gz

cd pocketsphinx-5prealpha

./configure
make
make install

cd ..

########## install english acoustics files
tar -xzvf sources/cmusphinx-en-us-8khz-5.1.tar.gz

#clean up


