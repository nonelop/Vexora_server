import socket, json, threading, config
from client_handler import new_client_handler

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((config.SERVER_IP, config.SERVER_PORT))

    connections_thread = threading.Thread(
        target=new_client_handler.new_connection_handler(sock)
    )

    connections_thread.start()