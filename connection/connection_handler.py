import socket, threading, json
from proto import authorization_method, message_method
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
            # Загрузка запроса

            request = connection.recv(4096).decode(encoding="utf-8")
            request = json.loads(request)

            method = request["method"]
            auth = request["auth"]

            # Если запрос на авторизацию, пропуск без токена

            if method == "authorization":
                result = authorization_method.authorization_method_parse(request)

            # Проверка токена и обработка

            token_valid = authorizator.check_token(
                user_id=auth["user_id"], token=auth["token"]
            )

            if token_valid:
                match method:
                    case "message":
                        result = message_method.message_method_parse(request)
                    case _:
                        result = {"status": "400 Bad Request", "data": []}

            else:
                result = {"status": "401 Unauthorized", "data": []}

            result_str = json.dumps(result)
            result_bytes = result_str.encode(encoding="utf-8")

            connection.sendall(result_bytes)

        except:
            break
