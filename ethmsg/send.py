import os
from pathlib import Path

import json
import web3
from string import Template

from eth_account import Account
from web3 import Web3
from solc import compile_source

def send(endpoint, message):
    w3 = Web3(Web3.HTTPProvider(endpoint))

    account = Account()
    
    private_key = os.environ["ETH_MSG_PRIVATE_KEY"]
    address = account.privateKeyToAccount(private_key).address
    
    contract_source_code = '''
    pragma solidity ^0.4.21;
    
    contract Message {
      string public text;

      function Message() public {
        text = '$message';
      }

      function getText() public returns(string) {
        return text;
      }
    }
    '''

    contract_source_code = Template(contract_source_code).substitute({'message': message})
    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:Message']
    
    nonce = w3.eth.getTransactionCount(address, 'pending')

    Message = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    text_file = open("/tmp/fin.json", "w")
    text_file.write("%s" % json.dumps(contract_interface['abi']))
    text_file.close()
    
    tx = Message.constructor().buildTransaction({
        'from': address,
        'gas': w3.eth.estimateGas(Message.constructor().buildTransaction({'from': address})),
        'nonce': nonce,
        'gasPrice': w3.eth.gasPrice
    })

    signed_txn = w3.eth.account.signTransaction(tx, private_key=private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash, 10000)

    receipt_data = w3.eth.getTransactionReceipt(tx_hash)
    
    print("Message saved to contract:")
    print(receipt_data['contractAddress'])

    print("Transaction hash:")
    print(tx_hash.hex())

