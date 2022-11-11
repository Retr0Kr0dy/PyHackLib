#!/usr/bin/python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class EncryptAES:
    def Encrypt(block=bytes, key=bytes):
        cipher = AES.new(key, AES.MODE_CBC)
        data_result = cipher.encrypt(pad(block, AES.block_size))
        result = cipher.iv + data_result
        
        return result


class EncryptRSA:
    def Encrypt(block=bytes, public_key=bytes):
        public_key = serialization.load_pem_public_key(
            public_key,
            backend=default_backend()
        )

        encrypted = public_key.encrypt(block,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ) 

        return encrypted