from  utilities.web3_top_class import Web_Class_IPC
import redis
import time
import datetime
redis_handle = redis.StrictRedis( db=1 )

ipc_socket = "/home/pi/geth.ipc"
w3 = Web_Class_IPC(ipc_socket,redis_handle)
print(w3.__dict__)
print(w3.get_block_number())


def handle_event(event):
    print("event",event)
    
def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

def main():
    contract_object = w3.get_contract("hellow_world")
    #block_filter = w3.w3.eth.filter('latest')
    block_filter=contract_object.events.Update_Event.createFilter(fromBlock=0 ,toBlock='latest')
   
    x = block_filter.get_all_entries()
    print(len(x))
    for i in x:
       print(i)
       print(i.transactionHash)
       block_number = i.blockNumber
       print(block_number)
       print(w3.get_block(block_number).timestamp)
       print(time.time())
       
    log_loop(block_filter, 2)


main()
'''
web3.eth.blockNumber
web3.eth.getBlock(<blockNumber>0
hash = xxxx
web3.eth.getTransactionByBlock(hash,tx_id))
'''
