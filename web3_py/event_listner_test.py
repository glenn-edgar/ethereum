#from  utilities.web3_top_class import Web_Class_IPC
from utilities.event_listner_top_class import Event_Listner_Class_IPC
import redis
import time
import datetime
redis_handle = redis.StrictRedis( db=1 )

ipc_socket = "/home/pi/geth.ipc"






ev = Event_Listner_Class_IPC(ipc_socket,redis_handle)





print(ev.get_block_number())
ev.construct_loop_filter("hellow_world")
temp = ev.get_all_entries("hellow_world")
print(temp)

def event_handler(event):
   print(event)
   if event.blockNumber > 25:
      return False
   else:
      return True

ev.lastest_event_loop("hellow_world",event_handler)

