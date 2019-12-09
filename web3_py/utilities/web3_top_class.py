
from web3 import Web3
from web3.middleware import geth_poa_middleware


class Web_Class_IPC(object):

   def __init__(self,ipc_socket,signing_key):
       provider = Web3.IPCProvider(ipc_socket)
       self.w3 = Web3(provider)
       self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
       assert(self.w3.isConnected())
       self.signing_key = signing_key
       
       
   def send_currency(self, to_account_index, value):  # value in ether
       with open(self.signing_key) as keyfile:
           encrypted_key = keyfile.read()
           private_key = self.w3.eth.account.decrypt(encrypted_key, 'ready2go')
           signed_txn = self.w3.eth.account.signTransaction(dict(
               nonce=self.w3.eth.getTransactionCount(self.w3.eth.accounts[1]),
               gasPrice = self.w3.eth.gasPrice, 
               gas = 100000,
               to=self.w3.eth.accounts[to_account_index],
               value=self.w3.toWei(value,'ether')),
               private_key)
           rawHash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
           hexHash = self.w3.toHex(rawHash)            
           return self.w3.eth.waitForTransactionReceipt(hexHash)

   def get_block_number(self):
      return self.w3.eth.blockNumber
      
   def get_balance(self, account_index):
       return self.w3.fromWei(self.w3.eth.getBalance(self.w3.eth.accounts[account_index]),"ether")
       
   def get_accounts(self):
      return self.w3.eth.accounts