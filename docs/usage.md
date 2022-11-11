# <b><i>USAGE - PyHackLib python3</b></i>
# Cryptography

## Key Generation.
```python
from PyHackLib.Cryptography.KeyGeneration import *
```

AES key gen ; 
```python
AES_key = KeyGenAES.GenerateKey() # Generate AES key

KeyGenAES.GetKeyBytes(AES_key) # Get bytes of AES_key
KeyGenAES.GetKeyString(AES_key) # Get string of AES_key
```

RSA key gen ; 
```python
private_key, public_key = KeyGenRSA.GenerateKey() # Generate private and public keys

KeyGenRSA.GetKeyBytes(private_key) # Get bytes of RSA private key
KeyGenRSA.GetKeyString(private_key) # Get string of RSA private key

KeyGenRSA.GetKeyBytes(public_key) # Get bytes of RSA public key
KeyGenRSA.GetKeyString(public_key) # Get string of RSA public key
```

## Encryption.
```python
from PyHackLib.Cryptography.Encryption import *
```

AES encryption ;
```python
EncryptAES.Encrypt(bytes(block),bytes(AES_key))
```

RSA encryption ;
```python
EncryptRSA.Encrypt(bytes(block),bytes(public_key))
```

## Decryption.
```python
from PyHackLib.Cryptography.Decryption import *
```

AES decryption ;
```python
DecryptAES.Decrypt(bytes(block),bytes(AES_key))
```

RSA decryption ;
```python
DecryptRSA.Decrypt(bytes(block),bytes(private_key))
```

