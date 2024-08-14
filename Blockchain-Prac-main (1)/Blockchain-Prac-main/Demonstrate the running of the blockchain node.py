import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', nonce=100)  # Genesis block

    def create_block(self, nonce, previous_hash=None):
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash or self.chain[-1].compute_hash(),
            timestamp=time(),
            transactions=self.current_transactions,
            nonce=nonce
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

    def proof_of_work(self, last_nonce):
        nonce = 0
        while True:
            hash_result = hashlib.sha256(f"{last_nonce}{nonce}".encode()).hexdigest()
            if hash_result[:4] == '0000':  # Example difficulty level
                return nonce
            nonce += 1

    def mine_block(self):
        last_block = self.chain[-1]
        last_nonce = last_block.nonce
        nonce = self.proof_of_work(last_nonce)
        self.add_transaction(sender='0', recipient='miner', amount=1)  # Reward for mining
        self.create_block(nonce, previous_hash=last_block.compute_hash())

    def display_chain(self):
        for block in self.chain:
            print(f"Block #{block.index} - Hash: {block.compute_hash()}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Transactions: {block.transactions}")
            print(f"Nonce: {block.nonce}")
            print('')

# Running the Blockchain Node
if __name__ == "__main__":
    blockchain = Blockchain()
    print("Starting Blockchain Node...\n")

    # Add some transactions
    blockchain.add_transaction(sender="Alice", recipient="Bob", amount=50)
    blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=30)
    
    print("Mining block...")
    blockchain.mine_block()

    blockchain.display_chain()
