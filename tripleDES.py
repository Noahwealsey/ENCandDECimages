from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import time

def generate_triple_des_key():
    # Choose between 16 bytes (DES-EDE) or 24 bytes (DES-EDE3)
    key_size = 16 if DES3.key_size == 16 else 24
    return get_random_bytes(key_size)

def encrypt(data, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(data, DES3.block_size)
    return cipher.encrypt(padded_data)

def decrypt_3des(encrypted_data, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data
