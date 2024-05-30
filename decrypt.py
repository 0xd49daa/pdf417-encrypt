import os
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from PIL import Image as PIL
from pdf417decoder import PDF417Decoder

SALT_SIZE = 16
KEY_SIZE = 32
ITERATIONS = 100000
BLOCK_SIZE = AES.block_size

def decrypt_data(encrypted_data, password):
    salt = encrypted_data[:SALT_SIZE]
    nonce = encrypted_data[SALT_SIZE:SALT_SIZE + BLOCK_SIZE]
    tag = encrypted_data[SALT_SIZE + BLOCK_SIZE:SALT_SIZE + 2 * BLOCK_SIZE]
    ciphertext = encrypted_data[SALT_SIZE + 2 * BLOCK_SIZE:]
    key = PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

def read_pdf417(image_path):
    image = PIL.open(image_path)
    decoder = PDF417Decoder(image)
    if decoder.decode() > 0:
        decoded = decoder.barcode_data_index_to_string(0)
        return b64decode(decoded)
    return None
