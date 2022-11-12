#!/usr/bin/python
import socket

def GetHostIp():
    return socket.gethostbyname(socket.gethostname())


class TCPConnecting:
    def Connect(host=str,port=int):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect ((host, port))

        return client
 