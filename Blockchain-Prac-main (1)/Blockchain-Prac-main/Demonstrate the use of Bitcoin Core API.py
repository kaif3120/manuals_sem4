#pip install bitcoinlib
#Use Python 3.9.12
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


# import requests
# import requests
# import json


# def get_wallet_balance(address):
#     url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'
#     response = requests.get(url)
#     data = response.json()
#     balance = data['balance'] / 10**8  # Convert from satoshis to BTC
#     return balance

# # Example Bitcoin address (replace with your own)
# address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
# balance = get_wallet_balance(address)
# print(f"Wallet Balance: {balance} BTC")

# def send_bitcoin(sender_private_key, sender_address, recipient_address, amount):
#     # Prepare transaction data
#     tx_data = {
#         "inputs": [{"addresses": [sender_address]}],
#         "outputs": [{"addresses": [recipient_address], "value": int(amount * 10**8)}]
#     }

#     # Create transaction
#     url = "https://api.blockcypher.com/v1/btc/main/txs/new"
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, data=json.dumps(tx_data), headers=headers)
#     tx = response.json()

#     # Normally, you'd sign the transaction with your private key here.
#     # For demonstration, we'll assume the signing is done.

#     # Send the signed transaction
#     send_url = f"https://api.blockcypher.com/v1/btc/main/txs/send"
#     response = requests.post(send_url, data=json.dumps(tx), headers=headers)
    
#     return response.json()

# # Replace with your own values
# sender_private_key = "your_private_key"
# sender_address = "sender_bitcoin_address"
# recipient_address = "recipient_bitcoin_address"
# amount = 0.001  # BTC

# tx_result = send_bitcoin(sender_private_key, sender_address, recipient_address, amount)
# print(f"Transaction Result: {tx_result}")

# def get_transaction_history(address):
#     url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/full"
#     response = requests.get(url)
#     transactions = response.json()["txs"]
#     return transactions

# # Example Bitcoin address
# address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
# transactions = get_transaction_history(address)

# for tx in transactions:
#     print(f"Transaction ID: {tx['hash']}")
#     print(f"Confirmed: {tx['confirmed']}")
#     print(f"Total Sent: {tx['total']/10**8} BTC")
#     print(f"Total Received: {tx['total']/10**8} BTC")
#     print("---------")



