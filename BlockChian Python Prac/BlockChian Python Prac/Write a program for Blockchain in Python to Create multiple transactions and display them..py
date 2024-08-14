import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.proof = proof
        self.hash = self.hash_block()

    def hash_block(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.proof}".encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.transactions = []

    def create_genesis_block(self):
        return Block(0, "0", [], 0)

    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})

    def add_block(self):
        last_block = self.chain[-1]
        proof = self.proof_of_work(last_block.proof)
        new_block = Block(len(self.chain), last_block.hash, self.transactions, proof)
        self.transactions = []
        self.chain.append(new_block)

    def proof_of_work(self, last_proof):
        proof = 0
        while not hashlib.sha256(f"{last_proof}{proof}".encode()).hexdigest().startswith("0000"):
            proof += 1
        return proof

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index} | Hash: {block.hash} | Transactions: {block.transactions}")

# Example usage
blockchain = Blockchain()
blockchain.add_transaction("Alice", "Bob", 50)
blockchain.add_block()
blockchain.add_transaction("Charlie", "Alice", 75)
blockchain.add_block()
blockchain.display_chain()
