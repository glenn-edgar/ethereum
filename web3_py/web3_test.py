from  utilities.web3_top_class import Web_Class_IPC


signing_key = '/mnt/ssd/ethereum/dev_data/keystore/UTC--2019-12-08T20-29-05.205871190Z--75dca28623f88b105b8d0c718b4bfde0f1568688'
ipc_socket = "/home/pi/geth.ipc"
w3 = Web_Class_IPC(ipc_socket,signing_key)
print(w3.get_block_number())
print(w3.get_accounts())
print(w3.get_balance(1))
print(w3.send_currency(2,.5))
print(w3.get_balance(1))
print(w3.get_balance(2))