import socket

#########################################
# Functionality is based on
# Title: Socket Programming HOWTO
# Author: Gordon McMillan
# Code is based on:
# Source URL: https://docs.python.org/3/howto/sockets.html
#########################################

# Connection details
HOST = 'localhost'
PORT = 4444

# Start server socket and listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("Server listening on: {} on port {}".format(HOST, PORT))

# Accept client connections
(client, address) = server.accept()
print("Connected by {}".format(address))
print("Waiting for message...")

# Handle message sending and receiving
while True:
    incomingMessage = client.recv(1024).decode()
    if incomingMessage:
        # Client has quit the connection
        if incomingMessage == '/q':
            client.close()
            print("Client Closed")
            break
        else:
            print(incomingMessage)

    sendMessage = input(">")
    client.send(sendMessage.encode())
    # Server quit connection
    if sendMessage == '/q':
        break

server.close()
