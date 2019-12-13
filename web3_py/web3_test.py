from  utilities.web3_top_class import Web_Class_IPC
import redis
import datetime


redis_handle = redis.StrictRedis( db=1 )

signing_key = '/mnt/ssd/ethereum/dev_data/keystore/UTC--2019-12-08T20-29-05.205871190Z--75dca28623f88b105b8d0c718b4bfde0f1568688'
ipc_socket = "/home/pi/geth.ipc"
w3 = Web_Class_IPC(ipc_socket,redis_handle,signing_key)
print(w3.get_block_number())
print(w3.get_accounts())
print(w3.get_balance(1))
#print(w3.send_currency(2,.5))
print(w3.get_balance(1))
print(w3.get_balance(2))

contract_object = w3.get_contract("hellow_world")

print(w3.read_contract_data(contract_object, "printSomething" ))
now = datetime.datetime.now()
tx_reciept = w3.transact_contract_data(contract_object, "changeText" ,now.isoformat())
print(tx_reciept.blockNumber)
print(w3.read_contract_data(contract_object, "printSomething" ))
rich_logs = contract_object.events.Update_Event().processReceipt(tx_reciept)
print(rich_logs)
print(len(rich_logs))
print(rich_logs[0]["args"])
print(rich_logs[0]["args"].keys())
x = rich_logs[0].__dict__
print(list(x.keys()))
