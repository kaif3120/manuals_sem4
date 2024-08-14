import hashlib
import time

class Block(object):
    def __init__(self, index, proof_number, previous_hash, data, timestamp=None):
        self.index = index
        self.proof_number = proof_number
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def compute_hash(self):
        string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)
        return hashlib.sha256(string_block.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.build_genesis()

    def build_genesis(self):
        self.build_block(proof_number=0, previous_hash='0')

    def build_block(self, proof_number, previous_hash):
        block = Block(
            index=len(self.chain) + 1,  # Index starts from 1
            proof_number=proof_number,
            previous_hash=previous_hash,
            data=self.current_data
        )
        self.current_data = []
        self.chain.append(block)
        return block

    @staticmethod
    def confirm_validity(block, previous_block):
        if previous_block.index + 1 != block.index:
            return False
        elif previous_block.compute_hash != block.previous_hash:
            return False
        elif block.timestamp <= previous_block.timestamp:
            return False
        return True

    def get_data(self, sender, receiver, amount):
        self.current_data.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return True

    @staticmethod
    def proof_of_work(last_proof):
        # Implement a simple proof of work algorithm
        proof = 0
        while not (hashlib.sha256(f"{last_proof}{proof}".encode()).hexdigest().startswith('0000')):
            proof += 1
        return proof

    @property
    def latest_block(self):
        return self.chain[-1]

    def chain_validity(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if not self.confirm_validity(current_block, previous_block):
                return False
        return True

    def block_mining(self, details_miner):
        self.get_data(
            sender="0",  # '0' implies that this node has created a new block
            receiver=details_miner,
            amount=1  # Mining reward
        )
        last_block = self.latest_block
        last_proof_number = last_block.proof_number
        proof_number = self.proof_of_work(last_proof_number)
        last_hash = last_block.compute_hash
        block = self.build_block(proof_number, last_hash)
        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def get_block_object(block_data):
        return Block(
            block_data['index'],
            block_data['proof_number'],
            block_data['previous_hash'],
            block_data['data'],
            timestamp=block_data['timestamp']
        )

# Demonstration
if __name__ == "__main__":
    blockchain = Blockchain()
    print("GET READY MINING ABOUT TO START")
    print(blockchain.chain)
    
    last_block = blockchain.latest_block
    last_proof_number = last_block.proof_number
    proof_number = blockchain.proof_of_work(last_proof_number)
    
    blockchain.get_data(
        sender="0",
        receiver="Sana",
        amount=1
    )
    
    last_hash = last_block.compute_hash
    block = blockchain.build_block(proof_number, last_hash)
    
    print("WOW, MINING HAS BEEN SUCCESSFUL!")
    print(blockchain.chain)
