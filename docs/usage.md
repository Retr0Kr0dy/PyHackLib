# <b><i>USAGE - PyHackLib python3</b></i>
# Cryptography

## Key Generation.
```python
from PyHackLib.Cryptography.KeyGeneration import * # Import key generation class
```

AES key gen ; 
```python
AES_key = KeyGenAES.GenerateKey() # Generate AES key

KeyGenAES.GetKeyBytes(AES_key) # Get bytes of AES_key
KeyGenAES.GetKeyString(AES_key) # Get string of AES_key
```

RSA key gen ; 
```python
private_key, public_key = KeyGenRSA.GenerateKey(int(size)) # Generate private and public keys, size should be an int in 1024, 2048, 3072, 4096

KeyGenRSA.GetKeyBytes(private_key) # Get bytes of RSA private key
KeyGenRSA.GetKeyString(private_key) # Get string of RSA private key

KeyGenRSA.GetKeyBytes(public_key) # Get bytes of RSA public key
KeyGenRSA.GetKeyString(public_key) # Get string of RSA public key
```

## Encryption.
```python
from PyHackLib.Cryptography.Encryption import * # Import encryption class
```

AES encryption ;
```python
EncryptAES.Encrypt(bytes(block),bytes(AES_key)) # Encrypt block bytes unsing AES_key
```

RSA encryption ;
```python
EncryptRSA.Encrypt(bytes(block),bytes(public_key)) # Encrypt block bytes using public_key
```

## Decryption.
```python
from PyHackLib.Cryptography.Decryption import * # import decryption class
```

AES decryption ;
```python
DecryptAES.Decrypt(bytes(block),bytes(AES_key)) # Decrypt block bytes unsing AES_key
```

RSA decryption ;
```python
DecryptRSA.Decrypt(bytes(block),bytes(private_key)) # Decrypt block bytes using private_key
```

# Sockets

## Listener.
```python
from PyHackLib.Sockets.Listener import * # Import Listener class
```

Get Host IP ;
```python
host = PyHackLib.Sockets.Listener.GetHostIp() # Get current host IP
```

TCP Listen ; 
```python
listener = PyHackLib.Sockets.Listener.TCPListening(str(host),int(port)) # Create a listener on <address, port>
```

## Connect.
```python
from PyHackLib.Sockets.Connect import * # Import Connect class
```

TCP Connect ;
```python
PyHackLib.Sockets.Connect.TCPConnecting(str(host),int(port)) # Connect to listener on <address, port>
```

## Handle.

```python

from PyHackLib.Sockets.Handle import * # Import Handle class

```



TCP Handle ;

```python

client, address = PyHackLib.Sockets.Connect.TCPHandling.AcceptClient(listener) # Accept client on listener socket 
PyHackLib.Sockets.Connect.TCPHandling.ReceiveMesesage(client) # Receive message from client
PyHackLib.Sockets.Connect.TCPHandling.SendMessage(client, bytes(message)) # Send message to client 
```




