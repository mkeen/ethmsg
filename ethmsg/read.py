import os
from pathlib import Path

import json
import web3
from string import Template

from eth_account import Account
from web3 import Web3

base_abi = json.loads('[{"constant": true, "inputs": [], "name": "text", "outputs": [{"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}]')

def read(endpoint, contract_address):
    w3 = Web3(Web3.HTTPProvider(endpoint))
    account = Account()
    private_key = os.environ["ETH_MSG_PRIVATE_KEY"]
    address = account.privateKeyToAccount(private_key).address
    contract = w3.eth.contract(address=contract_address, abi=base_abi)
    
    nonce = w3.eth.getTransactionCount(address)
    tx = contract.functions.text().call({'from': address})

    print("Message:")
    print(tx)

