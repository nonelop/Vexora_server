def message_method_parse(request: dict):

    data = request["data"]

    match request["operaton"]:
        case "send_message":
            result = send_message(data["from_user_id"], data["to_user_id"], data["message"])


def send_message(from_user_id: int, to_user_id: int, message: str):

    pass