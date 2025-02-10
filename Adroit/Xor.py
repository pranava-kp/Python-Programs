def vernam_encrypt(plain_text, key):
    return ''.join([chr(ord(c) ^ ord(k)) for c, k in zip(plain_text, key)])
def vernam_decrypt(cipher_text, key):
    return vernam_encrypt(cipher_text, key) # XOR is reversible