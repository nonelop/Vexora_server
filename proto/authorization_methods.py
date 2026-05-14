from database.database import write_new_user, check_username


def authorization_methods_parse(request: dict):

    data = request["data"]

    match request["operation"]:
        case "register_new_user":
            result = register_new_user(data=data)
            return result
        case "check_user_username":
            result = check_user_username(username=data["username"])
            return result


def register_new_user(data: dict):

    write_new_user(data=(data["username"]))
    result = {"status": "OK", "data": [], "error": ""}

    return result


def check_user_username(username: str):

    is_exist = check_username(username)
    result = {"status": "OK", "data": [is_exist], "error": ""}

    return result