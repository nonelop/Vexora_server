import socket, threading, json
from proto import authorization_method, message_method


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
            json_request = json.loads(request)

            method = json_request["method"]

            match method:
                case "authorization":
                    result = authorization_method.authorization_method_parse(
                        json_request
                    )
                case "message":
                    result = message_method.message_method_parse(
                        json_request
                    )

            result_str = json.dumps(result)
            result_bytes = result_str.encode(encoding="utf-8")

            connection.sendall(result_bytes)

        except:
            break
