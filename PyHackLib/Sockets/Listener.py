#!/usr/bin/python
import socket

def GetHostIp():
    return socket.gethostbyname(socket.gethostname())


class TCPListening:
    def Listen(host=str,port=int):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind((host, port))
        listener.listen()

        return listener
 