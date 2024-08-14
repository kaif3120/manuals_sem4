import hashlib

def sha256(message):
    """Compute the SHA-256 hash of a message."""
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
    """Perform mining by finding a nonce that produces a hash with a given difficulty."""
    assert difficulty >= 1
    prefix = '1' * difficulty  # Create the prefix for the hash to match
    print(f"Mining for a hash with difficulty {difficulty} (prefix '{prefix}')...")

    for i in range(1000):
        # Create a digest with the current nonce
        digest = sha256(f"{message}{i}")
        if digest.startswith(prefix):
            print(f"After {i} iterations, found nonce: {i} with hash: {digest}")
            return digest

    print("No valid nonce found after 1000 iterations.")
    return None

# Test the mining function
mine("test message", 2)
