from web3 import Web3
from web3.middleware import geth_poa_middleware
import sys
import json
import redis

contract_name = sys.argv[1]

ipc_socket = "/home/pi/geth.ipc"
provider = Web3.IPCProvider(ipc_socket)
w3 = Web3(provider)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
assert(w3.isConnected())
w3.eth.defaultAccount = w3.eth.accounts[0]
abi_file_name = "solc_output/"+contract_name+".abi"
abi_file = open(abi_file_name,"r")
abi_data = abi_file.read()

abi_json = json.loads(abi_data)

bin_file_name = "solc_output/"+contract_name+".bin"
bin_file = open(bin_file_name,"r")
bytecode = bin_file.read()

contract_object = w3.eth.contract(abi=abi_json, bytecode=bytecode)
tx_hash = contract_object.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
greeter = w3.eth.contract(
     address=tx_receipt.contractAddress,
     abi=abi_json
 )
print(greeter.functions.printSomething().call())
tx_hash = greeter.functions.changeText("new text").transact({
        'from': w3.eth.accounts[0],
    })
    
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)   
print(greeter.functions.printSomething().call())