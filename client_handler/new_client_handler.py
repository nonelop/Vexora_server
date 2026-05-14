import socket, threading

def new_connection_handler(sock: socket.socket):

    sock.listen(100)

    connection, address = sock.accept()