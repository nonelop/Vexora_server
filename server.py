import socket, json, threading
from requests_parse import database_requests

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('192.168.2.5', 5050))

    sock.listen(3)
    print("listen to 192.168.2.5:5050")

    connection, address = sock.accept()
    print(address)


    raw_message = connection.recv(4096)
    message = raw_message.decode(encoding="utf-8")
    json_message = json.loads(message)

    req_type = json_message["req_type"]
    operation = json_message["operation"]
    values = json_message.get("values", 0)

    operation_result = {
        "status": "processing",
        "values": [],
        "error": False,
        "error_str": ""
    }

    match req_type:

        case "database":
            operation_result = database_requests.database_req_parse(request=json_message)

    operation_result_json = json.dumps(operation_result)
    operation_result_bytes = operation_result_json.encode(encoding="utf-8")


    connection.send(operation_result_bytes)

