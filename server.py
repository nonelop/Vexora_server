import socket, json
from database import database

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
            match operation:
                case "write":
                    database.write_new_user(values=(values["username"], values["password"]))
                    operation_result["status"] = "successful"
                case "check_username":
                    result = database.check_username(username=values["username"])
                    operation_result["status"] = "successful"
                    operation_result["values"].append(result)

    operation_result_json = json.dumps(operation_result)
    operation_result_bytes = operation_result_json.encode(encoding="utf-8")


    connection.send(operation_result_bytes)

