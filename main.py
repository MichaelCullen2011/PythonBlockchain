import hashlib
import random
import string
import json
import binascii
import numpy as np
import pylab as pl
import pandas as pd
import logging
import datetime
import collections

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from classes.Block import Block
from classes.Client import Client
from classes.Transaction import Transaction
from classes.Mining import Mining


'''Clients'''
Alice = Client()
Bob = Client()
Charlie = Client()
Eve = Client()


'''Transactions'''
transactions = []
def display_transaction(transaction):
    dict = transaction.to_dict()
    print ("sender: " + dict['sender'])
    print ('-----')
    print ("recipient: " + dict['recipient'])
    print ('-----')
    print ("value: " + str(dict['value']))
    print ('-----')
    print ("time: " + str(dict['time']))
    print ('-----')

t0 = Transaction(
    "Genesis",
    Alice.identity,
    400.0
)

t1 = Transaction(Alice, Bob.identity, 100.0)
t1.sign_transaction()
transactions.append(t1)
t2 = Transaction(Alice, Charlie.identity, 100.0)
t2.sign_transaction()
transactions.append(t2)
t3 = Transaction(Alice, Eve.identity, 100.0)
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(Eve, Bob.identity, 9.0)
t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(Bob, Charlie.identity, 2.0)
t5.sign_transaction()
transactions.append(t5)
t6 = Transaction(Charlie, Alice.identity, 1.0)
t6.sign_transaction()
transactions.append(t6)
t7 = Transaction(Alice, Bob.identity, 2.0)
t7.sign_transaction()
transactions.append(t7)
t8 = Transaction(Eve, Alice.identity, 1.0)
t8.sign_transaction()
transactions.append(t8)
t9 = Transaction(Bob, Alice.identity, 3.0)
t9.sign_transaction()
transactions.append(t9)
t10 = Transaction(Bob, Charlie.identity, 4.0)
t10.sign_transaction()
transactions.append(t10)

# for transaction in transactions:
#     display_transaction(transaction)
#     print ('--------------')


'''Blockchain'''
Blockchain = []

def dump_blockchain(self):
    print ("Number of blocks in the chain: " + str(len(self)))
    for x in range(len(Blockchain)):
        block_temp = Blockchain[x]
        print ("block # " + str(x))

        for transaction in block_temp.verified_transactions:
            display_transaction(transaction)
            print ('--------------')
        print ('=====================================')


'''Initialise Block'''
block0 = Block()
block0.previous_block_hash = None
block0.Nonce = None
block0.verified_transactions.append(t0)

digest = hash(block0)
last_block_hash = digest

Blockchain.append(block0)
dump_blockchain(Blockchain)


'''Mining''' 
Mining.mine(message="test message", difficulty=2)


'''Adding Blocks'''
last_transaction_index = 0

# Miner 1 Adds a Block
block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # Validate Transaction
    block.verified_transactions.append(temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash
block.Nonce = Mining.mine(block, 2)
digest = hash(block)
Blockchain.append(block)
last_block_hash = digest

# Miner 2 Adds a Block
block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    block.verified_transactions.append(temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash
block.Nonce = Mining.mine(block, 2)
digest = hash (block)
Blockchain.append(block)
last_block_hash = digest

# Miner 3 Adds a Block
block = Block()
for i in range(3):
   temp_transaction = transactions[last_transaction_index]
   block.verified_transactions.append(temp_transaction)
   last_transaction_index += 1

block.previous_block_hash = last_block_hash
block.Nonce = Mining.mine(block, 2)
digest = hash(block)
Blockchain.append(block)
last_block_hash = digest


dump_blockchain(Blockchain)
print("Number of Blocks in Blockchain (including genesis): ", len(Blockchain))


