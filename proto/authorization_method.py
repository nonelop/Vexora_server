from database import database
import hashlib, secrets
from datetime import datetime


def authorization_method_parse(request: dict):

    data = request["data"]

    match request["operation"]:
        case "user.register":
            result = user_register(data=data)
            return result
        case "check.username":
            result = check_username(username=data["username"])
            return result
        case "token.generate":
            result = token_generate(user_id=data["user_id"])
            return result


def user_register(data: dict):

    date = datetime.now()

    is_exist = check_username(username=data["username"])["data"][0]

    if is_exist:
        return {"status": "409 Conflict", "data": []}
    
    else:
        database.write_new_user(
            username=data["username"], reg_time=date.strftime("%d_%m_%Y-%H:%M:%S")
        )
        return {"status": "200 OK", "data": []}
 

def token_generate(user_id: int):

    token = secrets.token_hex(32)
    raw_token_hash = hashlib.sha256(token.encode())
    token_hash = raw_token_hash.hexdigest()

    database.write_new_token(data=(user_id, token_hash))

    result = {"status": "200 OK", "data": [token]}

    return result


def check_username(username: str):

    is_exist = database.check_username(username)
    result = {"status": "200 OK", "data": [is_exist]}

    return result
