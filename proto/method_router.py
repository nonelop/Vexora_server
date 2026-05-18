from proto import authorization_method, message_method
from connection import authorizator

def method_route(request: dict):

    method = request["method"]
    auth = request["auth"]

    if method == "authorization":
        result = authorization_method.authorization_method_parse(request)
        return result
    else:
        is_token_valid = authorizator.check_token(auth["user_id"], auth["token"])

        if is_token_valid:
            match method:
                case "message":
                    result = message_method.message_method_parse(request)
                    return result
                case _:
                    return {"status": "400 Bad Request", "data": []}
        else:
            return {"status": "401 Unauthorized", "data": []}


