from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time

def generate_aes_key(key_size):
    return get_random_bytes(key_size // 8)

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data, AES.block_size)
    return cipher.encrypt(padded_data)

def decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    dec_data = cipher.decrypt(data)
    dec_data = unpad(dec_data, AES.block_size)
    return  dec_data
