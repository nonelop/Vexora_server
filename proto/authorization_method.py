from database import database
import hashlib, secrets


def authorization_method_parse(request: dict):

    data = request["data"]

    match request["operation"]:
        case "register_new_user":
            result = register_new_user(data=data)
            return result
        case "check_user_username":
            result = check_user_username(username=data["username"])
            return result
        case "generate_token":
            result = generate_token(user_id=data["user_id"])
            return result


def register_new_user(data: dict):

    database.write_new_user(data=(data["username"]))
    result = {"status": "200 OK", "data": []}

    return result


def generate_token(user_id: int):

    token = secrets.token_hex(32)
    raw_token_hash = hashlib.sha256(token.encode())
    token_hash = raw_token_hash.hexdigest()

    database.write_new_token(data=(user_id, token_hash))

    result = {"status": "200 OK", "data": [token]}

    return result


def check_user_username(username: str):

    is_exist = database.check_username(username)
    result = {"status": "200 OK", "data": [is_exist]}

    return result