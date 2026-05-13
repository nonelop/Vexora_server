import socket, json, threading
from proto import autorisation_methods

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('192.168.2.5', 5050))

    sock.listen(3)
    print("listen to 192.168.2.5:5050")

    connection, address = sock.accept()
    print(address)


    message = connection.recv(4096).decode(encoding="utf-8")
    json_message = json.loads(message)

    method = json_message["method"]


    match method:

        case "autorisation":
            operation_result = autorisation_methods.autorisation_methods_parse(request=json_message)

    operation_result_json = json.dumps(operation_result)
    operation_result_bytes = operation_result_json.encode(encoding="utf-8")


    connection.send(operation_result_bytes)

