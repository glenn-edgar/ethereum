from  utilities.web3_top_class import  Web_Class_IPC
import redis
import datetime
import time


redis_handle = redis.StrictRedis( db=1 )
ipc_socket = "/home/pi/geth.ipc"
signing_key = '/mnt/ssd/ethereum/dev_data/keystore/UTC--2019-12-08T20-29-05.205871190Z--75dca28623f88b105b8d0c718b4bfde0f1568688'
w3 = Web_Class_IPC(ipc_socket,redis_handle,signing_key)
web3 = w3.w3    
received_messages = []

sender = web3.geth.shh.new_key_pair()
sender_pub = web3.geth.shh.get_public_key(sender)

receiver = web3.geth.shh.new_key_pair()
receiver_pub = web3.geth.shh.get_public_key(receiver)
topic = '0x13370000'
payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

shh_filter = web3.geth.shh.new_message_filter({
        'privateKeyID': receiver,
        'sig': sender_pub,
        'topics': [topic,"0x12345678","0x00000000"],  #00000000 is a none topic
        'allowP2P':True
    }, )


web3.geth.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2000,
        'payload': payloads[0],
        'topic': topic,
        'pubKey': receiver_pub
    })
    
time.sleep(1)
web3.geth.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2000,
        'payload': payloads[1],
        'topic': "0x12345678",
        'pubKey': receiver_pub
    })
    
time.sleep(1)
web3.geth.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2000,
        'payload': payloads[0],
        
        'pubKey': receiver_pub
    })
   
time.sleep(1)
received_messages = web3.geth.shh.get_filter_messages(shh_filter)
print(len(received_messages))

message = received_messages[0]

print(message["payload"].decode())
print(message["topic"].hex())

message = received_messages[1]

print(message["payload"].decode())
print(message["topic"].hex())

message = received_messages[2]

print(message["payload"].decode())
print(message["topic"].hex())

'''
import pytest
import time

from hexbytes import (
    HexBytes,
)


def test_shh_sync_filter_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    with pytest.warns(DeprecationWarning):
        sender = web3.shh.newKeyPair()
        sender_pub = web3.shh.getPublicKey(sender)

        receiver = web3.shh.newKeyPair()
        receiver_pub = web3.shh.getPublicKey(receiver)

        topic = '0x13370000'
        payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

        shh_filter = web3.shh.newMessageFilter({
            'privateKeyID': receiver,
            'sig': sender_pub,
            'topics': [topic]
        })

        web3.shh.post({
            'sig': sender,
            'powTarget': 2.5,
            'powTime': 2,
            'payload': payloads[0],
            'pubKey': receiver_pub
        })
        time.sleep(1)

        web3.shh.post({
            'sig': sender,
            'powTarget': 2.5,
            'powTime': 2,
            'payload': payloads[1],
            'topic': topic,
            'pubKey': receiver_pub
        })
        time.sleep(1)

        received_messages = shh_filter.get_new_entries()
        assert len(received_messages) == 1

        message = received_messages[0]

        assert message["payload"] == HexBytes(payloads[1])
        assert message["topic"] == HexBytes(topic)


def test_shh_sync_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    sender = web3.shh.new_key_pair()
    sender_pub = web3.shh.get_public_key(sender)

    receiver = web3.shh.new_key_pair()
    receiver_pub = web3.shh.get_public_key(receiver)

    topic = '0x13370000'
    payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

    shh_filter = web3.shh.new_message_filter({
        'privateKeyID': receiver,
        'sig': sender_pub,
        'topics': [topic]
    })

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[0],
        'pubKey': receiver_pub
    })
    time.sleep(1)

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[1],
        'topic': topic,
        'pubKey': receiver_pub
    })
    time.sleep(1)

    received_messages = shh_filter.get_new_entries()
    assert len(received_messages) == 1

    message = received_messages[0]

    assert message["payload"] == HexBytes(payloads[1])
    assert message["topic"] == HexBytes(topic)


def test_shh_async_filter_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    received_messages = []

    with pytest.warns(DeprecationWarning) as warnings:
        sender = web3.shh.newKeyPair()
        sender_pub = web3.shh.getPublicKey(sender)

        receiver = web3.shh.newKeyPair()
        receiver_pub = web3.shh.getPublicKey(receiver)

        topic = '0x13370000'
        payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

        shh_filter = web3.shh.newMessageFilter({
            'privateKeyID': receiver,
            'sig': sender_pub,
            'topics': [topic]
        }, poll_interval=0.5)
        watcher = shh_filter.watch(received_messages.extend)

        web3.shh.post({
            'sig': sender,
            'powTarget': 2.5,
            'powTime': 2,
            'payload': payloads[0],
            'topic': topic,
            'pubKey': receiver_pub
        })
        time.sleep(1)

        web3.shh.post({
            'sig': sender,
            'powTarget': 2.5,
            'powTime': 2,
            'payload': payloads[1],
            'pubKey': receiver_pub
        })
        time.sleep(1)

        assert len(received_messages) == 1

        message = received_messages[0]

        assert message["payload"] == HexBytes(payloads[0])
        assert message["topic"] == HexBytes(topic)

        assert len(warnings) == 5

        watcher.stop()


def test_shh_async_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    received_messages = []

    sender = web3.shh.new_key_pair()
    sender_pub = web3.shh.get_public_key(sender)

    receiver = web3.shh.new_key_pair()
    receiver_pub = web3.shh.get_public_key(receiver)

    topic = '0x13370000'
    payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

    shh_filter = web3.shh.new_message_filter({
        'privateKeyID': receiver,
        'sig': sender_pub,
        'topics': [topic]
    }, poll_interval=0.5)
    watcher = shh_filter.watch(received_messages.extend)

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[0],
        'topic': topic,
        'pubKey': receiver_pub
    })
    time.sleep(1)

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[1],
        'pubKey': receiver_pub
    })
    time.sleep(1)

    assert len(received_messages) == 1

    message = received_messages[0]

    assert message["payload"] == HexBytes(payloads[0])
    assert message["topic"] == HexBytes(topic)

    watcher.stop()


def test_shh_remove_filter_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    with pytest.warns(DeprecationWarning):

        receiver = web3.shh.newKeyPair()
        receiver_pub = web3.shh.getPublicKey(receiver)

        payload = web3.toHex(text="test message :)")
        shh_filter = web3.shh.newMessageFilter({'privateKeyID': receiver})

        web3.shh.post({
            'powTarget': 2.5,
            'powTime': 2,
            'payload': payload,
            'pubKey': receiver_pub
        })
        time.sleep(1)

        message = shh_filter.get_new_entries()[0]
        assert message["payload"] == HexBytes(payload)

        assert web3.shh.deleteMessageFilter(shh_filter.filter_id)

        try:
            web3.shh.getMessages(shh_filter.filter_id)
            assert False
        except:
            assert True


def test_shh_remove_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    receiver = web3.shh.new_key_pair()
    receiver_pub = web3.shh.get_public_key(receiver)

    payload = web3.toHex(text="test message :)")
    shh_filter = web3.shh.new_message_filter({'privateKeyID': receiver})

    web3.shh.post({
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payload,
        'pubKey': receiver_pub
    })
    time.sleep(1)

    message = shh_filter.get_new_entries()[0]
    assert message["payload"] == HexBytes(payload)

    assert web3.shh.delete_message_filter(shh_filter.filter_id)

    try:
        web3.shh.get_messages(shh_filter.filter_id)
        assert False
    except:
        assert True
'''