import socket, json, threading, config
from connection import connection_handler

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((config.SERVER_IP, config.SERVER_PORT))

    connections = {}

    connections_thread = threading.Thread(
        target=connection_handler.new_connection_handler,
        args=(sock,)
    )

    connections_thread.start()
    connections_thread.join()