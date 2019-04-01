# A command line tool for persisting messages on the Ethereum blockchain forever

## Prep Your System (Ubuntu 14.04)
`sudo apt update`  
`sudo apt-get install build-essential checkinstall git`  

## Install Python 3.5 (unless you already have it)
`sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`  
`cd /usr/src`  
`wget https://www.python.org/ftp/python/3.5.6/Python-3.5.6.tgz`  
`sudo tar xzf Python-3.5.6.tgz`  
`cd Python-3.5.6`  
`sudo ./configure --enable-optimizations`  
`sudo make install`  
`cd ~`  

## Install Solidity 0.4.25 (unless you already have it)
### Install Cmake v3
`cd /usr/src`  
`wget https://github.com/Kitware/CMake/releases/download/v3.14.1/cmake-3.14.1.tar.gz`  
`tar -xvzf cmake-3.14.1.tar.gz`  
`cd cmake-3.14.1/`  
`./configure`  
`make`  
`make install`  
`cd ~`  

### Install Solc
`sudo apt-get install libboost-all-dev`  
`wget https://github.com/ethereum/solidity/archive/v0.4.25.tar.gz`  
`tar -xvzf v0.4.25.tar.gz`  
`cd solidity-0.4.25/`  
`./scripts/install_deps.sh`  
`echo ca82a6dff817ec66f44342007202690a93763949 > commit_hash.txt`  
`mkdir build && cd build`  
`cmake .. && make`  
`mv lllc/lllc /usr/bin/`  
`mv solc/solc /usr/bin/`

## Clone the repo
`git clone https://github.com/mkeen/ethmsg.git`  
`cd ethmsg`

## Build

`python3 setup.py sdist`

## Install

`sudo pip3 install dist/ethmsg-0.0.1.tar.gz`

## Use

Either set `ETH_MSG_PRIVATE_KEY` environment variable or prefix command. Either sign up for infura or set up local eth endpoint or use VPC. Load up an account with some ether and reference it with address arg (replace address below), or wait for prompt. Simple example:

### Send Message
`ETH_MSG_PRIVATE_KEY=_PRIV_KEY_HERE_ ethmsg --endpoint 'https://rinkeby.infura.io/v3/endpoint_id_here --message helloooo

### Retrieve Message
`ETH_MSG_PRIVATE_KEY=_PRIV_KEY_HERE_ ethrd --endpoint 'https://rinkeby.infura.io/v3/endpoint_id_here --contract CONTRACT_ID_HERE_FROM_ABOVE_SEND_COMMAND
