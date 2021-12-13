import socket

#########################################
# Functionality is based on
# Title: Socket Programming HOWTO
# Author: Gordon McMillan
# Code is based on:
# Source URL: https://docs.python.org/3/howto/sockets.html
#########################################

def attemptConnection(server_sock, host, port):
    """
    Attempt to establish a connection using the socket and destination given as arguments
    Returns True if the connection was successful and False if an exception was raised
    """
    try:
        server_sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("The connection was refused. Please make sure the server is running and firewall settings allow the connection.")
        return False
    except:
        print("Failed to connect")
        return False
    return True

def chatRoom(server_sock):
    """
    Takes a socket connection to the host server as an argument.
    Tells the user what server they are connected to and allows the user to send messages back and forth
    with the connected server.
    Either user can terminate the connection by sending /q as a message.
    """

    # Display information to user
    print("Connected to server: {} on port: {}".format(HOST, PORT))
    print("Type /q to quit")
    print("Enter message to send...")

    # Chat correspondence loop
    while True:
        # Send client message to server
        send_message = input(">")
        server_sock.send(send_message.encode())

        # Client wants to quit
        if send_message == '/q':
            break

        # Receive incoming message from server
        incoming_message = server_sock.recv(1024)
        if incoming_message:
            # Server wants to quit
            if incoming_message.decode() == '/q':
                print("Server Closed")
                break
            # Display the incoming message
            print(incoming_message.decode())

    # Close the used socket
    print("Connection ended")
    server_sock.close()


# Connection details and socket
HOST = 'localhost'
PORT = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Used for the connection exception handling
attempt = True
# Attempt to connect to server
while attempt:
    if attemptConnection(s, HOST, PORT):
        # No longer need to attempt to establish connection, open the chat room
        attempt = False
        chatRoom(s)
    else:
        # Connection not made
        while True:
            print("Would you like to retry the connection? y/n")
            retryConnection = input()
            if retryConnection.lower() == 'y':
                break
            elif retryConnection.lower() == 'n':
                print("Unable to establish connection. Exiting")
                attempt = False
                break
            else:
                print("Invalid input, please enter 'y' or 'n'")