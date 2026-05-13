from database.database import write_new_user, check_username, check_password


def database_req_parse(request: dict):

    request_values = request["values"]

    result = {"status": "processing", "values": [], "error": False, "error_str": ""}

    match request["operation"]:
        case "write":
            write_new_user(
                values=(request_values["username"], request_values["password"])
            )
            result["status"] = "successful"
        case "check_username":
            operation_result = check_username(username=request_values["username"])
            result["status"] = "successful"
            result["values"].append(operation_result)

    return result