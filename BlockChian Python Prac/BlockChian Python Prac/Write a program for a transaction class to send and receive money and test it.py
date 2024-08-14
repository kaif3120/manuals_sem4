class Transaction:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def send_money(self, amount):
        """Send money if sufficient balance is available."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return f"Sent ${amount}. New balance: ${self.balance}"

    def receive_money(self, amount):
        """Receive money and update the balance."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return f"Received ${amount}. New balance: ${self.balance}"

    def get_balance(self):
        """Return the current balance."""
        return f"Current balance: ${self.balance}"

# Testing the Transaction class
if __name__ == "__main__":
    # Create an instance of Transaction with an initial balance
    transaction = Transaction(initial_balance=1000)

    # Print the initial balance
    print(transaction.get_balance())

    # Send money
    print(transaction.send_money(200))

    # Receive money
    print(transaction.receive_money(300))

    # Attempt to send more money than available
    try:
        print("Attempting to send $1200...")
        print(transaction.send_money(1200))
    except ValueError as e:
        print("Error:", e)

    # Print the final balance
    print(transaction.get_balance())
