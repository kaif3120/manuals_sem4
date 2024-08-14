import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Random import get_random_bytes

class Client:
    def __init__(self):
        # Generate RSA key pair
        self._private_key = RSA.generate(1024, get_random_bytes)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
    
    @property
    def identity(self):
        # Return the public key in DER format and then convert to hex
        return binascii.hexlify(self._public_key.export_key(format='DER')).decode('ascii')

# Create an instance of Client and print the identity
Alice = Client()
print(Alice.identity)
