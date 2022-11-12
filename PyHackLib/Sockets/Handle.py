#!/usr/bin/python
class TCPHandling: 
    def AccpetClient(listener):
        client, address = listener.accept()

        return client, address


    def ReceiveMesesage(client):
        try:
            it = client.recv(3072)

            return it
        except:
            client.close()

            return 1


    def SendMessage(client, message):
        try:
            client.send(message)

            return 0
        except:

            return 1