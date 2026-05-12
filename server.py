import socket, json
from database import database

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('192.168.2.5', 5050))

    sock.listen(3)
    print("listen to 192.168.2.5:5050")

    connection, address = sock.accept()
    print(address)

    while True:
        raw_message = connection.recv(4096)
        message = raw_message.decode(encoding="utf-8")
        json_message = json.loads(message)

        req_type = json_message["req_type"]
        operation = json_message["operation"]
        values = json_message.get("values", 0)

        match req_type:

            case "database":
                match operation:
                    case "write":
                        database.write_new_user(values=(values["username"], values["password"]))

        connection.send(b"1")

