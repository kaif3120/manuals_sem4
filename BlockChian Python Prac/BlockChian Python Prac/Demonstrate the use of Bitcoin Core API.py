from bitcoinlib.wallets import Wallet

# Create a new wallet named 'Wallet3'
w = Wallet.create('Wallet3')

# Get the first key from the wallet and print the associated address
key1 = w.get_key()
print(f"Address: {key1.address}")

# Scan the blockchain for transactions and update UTXOs
w.scan()

# Print wallet information including balances and transactions
print(w.info())
