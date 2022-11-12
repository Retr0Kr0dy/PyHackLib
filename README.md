# <b>PyHackLib</b>
### <b><i>version 0.1.0-dev_release</i></b>
#
## Summary

- ### [Purpose](https://github.com/Retr0Kr0dy/PyHackLib#purpose-1)

- ### [What's available for now](https://github.com/Retr0Kr0dy/PyHackLib#whats-available-for-now-1) 

 - ### [Usage](https://github.com/Retr0Kr0dy/PyHackLib/blob/main/docs/usage.md)

# Purpose

This lib purpose is to centralized most hacking used trick or setup or vuln or wathever you want to call it.

Fuck educational purpose only, but don't be dumb, don't fuck with russia.

## Cryptography.

This class serve for cryptographic needs like key generation for securing exchanges or cryptfuck a laptop, or key cracking.

For now, only main ciphers are implemented, such as `AES`, `RSA`, `XOR`, `Brainfuck` and `Malbolge` ( yes, some may look aged and/or useless, and your right, but idc ).

```python
from PyHackLib.Cryptography.KeyGeneration import * # or whatever you named it
```

## Sockets.

Socket class may be used to handle connection over TCP/UDP sockets betwen one or multiple targets.

## Wireless.

Wireless class mainly is a way to play with all wireless things nearby.
For now, only `Wifi` and `Bluetooth` are implemented, but further version will included things such as `IR`, `RFID`, `NFC`, `802.x`, etc...



# What's available for now 

## Cryptography.

AES - `KeyGen, Encrypt, Decrypt`

RSA - `KeyGen, Encrypt, Decrypt`

XOR - comming soon ...

Cracker - coming soon ...

Slicer/Deslicer - coming soon ...

## Sockets.

TCP - `Listener, Connect, Handle`

UDP - comming soon ...

## Wireless.

not for now (at least a month)

# Usage

Go check usage readme [here](https://github.com/Retr0Kr0dy/PyHackLib/blob/main/docs/usage.md)
