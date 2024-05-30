import os
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import pdf417gen

SALT_SIZE = 16
KEY_SIZE = 32
ITERATIONS = 100000
BLOCK_SIZE = AES.block_size

def encrypt_file(file_path, password):
    salt = get_random_bytes(SALT_SIZE)
    key = PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    encrypted_data = salt + cipher.nonce + tag + ciphertext
    return encrypted_data

def generate_pdf417(data, output_path):
    encoded_data = b64encode(data).decode('utf-8')
    barcode = pdf417gen.encode(encoded_data, columns=20, security_level=8)
    image = pdf417gen.render_image(barcode, scale=3)
    image.save(output_path)
