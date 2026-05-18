import socket, threading, json
from proto import method_router
from connection import authorizator


def new_connection_handler(sock: socket.socket):

    while True:
        print("Ожидание подключения.")

        sock.listen(100)
        connection, address = sock.accept()

        print("Новое подключение.")

        new_client_thread = threading.Thread(target=client_handler, args=(connection,))

        new_client_thread.start()


def client_handler(connection: socket.socket):

    while True:
        try:

            request = connection.recv(4096).decode(encoding="utf-8")
            request = json.loads(request)

            result = method_router.method_route(request)

            result_str = json.dumps(result)
            result_bytes = result_str.encode(encoding="utf-8")

            connection.sendall(result_bytes)

        except:
            break
