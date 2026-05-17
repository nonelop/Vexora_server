from database import database

def message_method_parse(request: dict):

    data = request["data"]

    match request["operation"]:
        case "message.send":
            result = send_message(
                chat_id=data["chat_id"],
                content_type=data["content_type"], 
                text=data["text"]
            )
            return result


def send_message(chat_id: int, content_type: str, text):

    database.write_new_message(chat_id, content_type, text)

    result = {"status": "200 OK", "data": []}

    return result