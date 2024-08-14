import hashlib
import datetime
import collections
import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes

class Client:
    def __init__(self):
        random = get_random_bytes
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
    
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.export_key(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.nonce = ""

    def dump_blockchain(self):
        print("Number of blocks in the chain: " + str(len(TPCoins)))
        for x in range(len(TPCoins)):
            block_temp = TPCoins[x]
            print("block # " + str(x))
            for transaction in block_temp.verified_transactions:
                display_transaction(transaction)
            print(' ')
            print('=====================================')

def display_transaction(transaction):
    trans_dict = transaction.to_dict()
    print("sender: " + trans_dict['sender'])
    print(' ---- ')
    print("recipient: " + trans_dict['recipient'])
    print(' ---- ')
    print("value: " + str(trans_dict['value']))
    print(' ---- ')
    print("time: " + str(trans_dict['time']))
    print(' ---- ')

def hash(block):
    block_string = str(block.__dict__).encode()
    return hashlib.sha256(block_string).hexdigest()

# Test the code
Dinesh = Client()
t0 = Transaction("Genesis", Dinesh.identity, 500.0)
block0 = Block()
block0.previous_block_hash = None
block0.nonce = None
block0.verified_transactions.append(t0)

digest = hash(block0)
last_block_hash = digest

TPCoins = []
TPCoins.append(block0)
block0.dump_blockchain()
