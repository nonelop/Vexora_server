import socket, json, threading, config
from proto import authorization_methods

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((config.SERVER_IP, config.SERVER_PORT))

    sock.listen(3)
    print("listen to 192.168.2.5:5050")

    connection, address = sock.accept()
    print(address)


    message = connection.recv(4096).decode(encoding="utf-8")
    json_message = json.loads(message)

    method = json_message["method"]


    match method:

        case "authorization":
            operation_result = authorization_methods.authorization_methods_parse(request=json_message)

    operation_result_json = json.dumps(operation_result)
    operation_result_bytes = operation_result_json.encode(encoding="utf-8")


    connection.send(operation_result_bytes)

