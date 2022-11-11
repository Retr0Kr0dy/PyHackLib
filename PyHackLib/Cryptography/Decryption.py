#!/usr/bin/python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class DecryptAES:
    def Decrypt(block=bytes, key=bytes):
        iv = block [:16]
        encrypted_data = block [16:]
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        result = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        return result


class DecryptRSA:
    def Decrypt(block=bytes, private_key=bytes):
        private_key = serialization.load_pem_private_key(
            private_key,
            password=None,
            backend=default_backend()
        )

        original_message = private_key.decrypt(block,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return original_message