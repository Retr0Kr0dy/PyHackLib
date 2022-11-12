#!/usr/bin/python
from Crypto.Random import get_random_bytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class KeyGenAES:
    def GenerateKey():
        key = get_random_bytes(32)
        
        return key

    def GetKeyBytes(key):
        key = bytes(key)

        return key
    
    def GetKeyString(key=bytes):
        key = str(key)[2:-1]

        return key


class KeyGenRSA:
    def GenerateKey(size=int):
        size=int(size)
   
        if size not in [1024,2048,3072,4096]:
            return "Wrong key size --- 1024 \ 2048 \ 3072 \ 4096"

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=size,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key =  public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return private_key, public_key

    def GetKeyBytes(key):
        bytes(key)

        return key

    def GetKeyString(key=bytes):
        key=key.decode()

        return key  