from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import time

def generate_rsa_keypair(key_size):
    return RSA.generate(key_size)

def encrypt(data, keypair):
    rsa_cipher = PKCS1_OAEP.new(keypair.publickey())
    encrypted_data = b""
    chunk_size = 86  
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        encrypted_chunk = rsa_cipher.encrypt(chunk)
        encrypted_data += encrypted_chunk
    return encrypted_data
