# PYTHON HACKING LIB
## Summary


###  <b>Cryptography</b>

<details><summary>KeyGeneration</summary>
<p>


</details>
</p>


<details><summary>Encryption</summary>
<p>


</details>
</p>


<details><summary>Decryption</summary>
<p>


</details>
</p>


<details><summary>Cracking</summary>
<p>


</details>
</p>


###  <b>Sockets</b>

<details><summary>Server</summary>
<p>

- [Listen]()
- [Connect]()

</details>
</p>
 
<details><summary>Client</summary>
<p>

- [Listen]()
- [Connect]()

</details>
</p>
 
 
<details><summary>Handling</summary>
<p>


</details>
</p>


###  <b>Wireless</b>

<details><summary>Wifi</summary>
<p>

- [Scanning]()
- [Deauth]()
- [FakeTwin]()
- [HandShakeInterception]()
- [KeyCracking]()

</details>
</p>
 
<details><summary>Bluetooth</summary>
<p>

  - [Scanning]()
  - [Dos]()

</details>
</p>
 



# Purpose

This lib purpose is to centralized most hacking used trick or setup or vuln or wathever you want to call it.

Fuck educational purpose only, but don't be dumb, don't fuck with russia.

## Cryptography

This class serve for cryptographic needs like key generation for securing exchanges or cryptfuck a laptop, or cracking key.

For now, only main ciphers are implemented, such as `AES`, `RSA`, `XOR`, `Brainfuck` and `Malbolge` ( yes, some may look aged and/or useless, and your right, but idc ).

```python
from python-hacking-lib import Cryptography # or whatever you named it
```

## Sockets

Socket class may be used to handle connection over TCP/UDP sockets betwen one or multiple targets.

## Wireless

Wireless class mainly is a way to play with all wireless things nearby.
For now, only `Wifi` and `Bluetooth` are implemented, but further version will included things such as `IR`, `RFID`, `NFC`, `802.x`, etc...