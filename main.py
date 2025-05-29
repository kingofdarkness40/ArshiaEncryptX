
# ArshiaEncryptX - Core Encryption Script
# Developed by a cybersecurity pentester

import hashlib

def arshia_encrypt(data: str, key: str) -> str:
    mix = key[::-1] + data + key
    hash1 = hashlib.sha3_512(mix.encode()).hexdigest()
    hash2 = hashlib.sha256((key + hash1).encode()).hexdigest()
    return hash2

if __name__ == "__main__":
    text = input("Enter your text: ")
    secret = input("Enter your key: ")
    encrypted = arshia_encrypt(text, secret)
    print("Encrypted:", encrypted)
