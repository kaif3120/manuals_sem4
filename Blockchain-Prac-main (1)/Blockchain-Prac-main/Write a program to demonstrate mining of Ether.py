import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.mine_block()

    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self):
        while not self.compute_hash().startswith('0' * self.difficulty):
            self.nonce += 1
        return self.compute_hash()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [Block(0, "0", "Genesis Block", difficulty)]
        self.difficulty = difficulty
        self.transactions = []

    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})

    def mine_pending_transactions(self, miner_address):
        self.add_transaction('Network', miner_address, 1)
        new_block = Block(len(self.chain), self.chain[-1].hash, self.transactions, self.difficulty)
        self.chain.append(new_block)
        self.transactions = []

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index} | Hash: {block.hash} | Transactions: {block.transactions} | Nonce: {block.nonce}")

# Example usage
blockchain = Blockchain()
blockchain.add_transaction("Alice", "Bob", 5)
blockchain.mine_pending_transactions("Miner1")
blockchain.add_transaction("Bob", "Charlie", 2)
blockchain.mine_pending_transactions("Miner2")
blockchain.display_chain()
