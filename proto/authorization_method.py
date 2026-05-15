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


def register_new_user(data: dict):

    database.write_new_user(data=(data["username"]))
    result = {"status": "OK", "data": [], "error": ""}

    return result


def token_exchange(user_id: int):

    has_token = database.check_has_token(user_id)


def check_user_username(username: str):

    is_exist = database.check_username(username)
    result = {"status": "OK", "data": [is_exist], "error": ""}

    return result