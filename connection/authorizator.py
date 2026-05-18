from database import database
import hashlib

def check_token(user_id: int, token: str):

    hash_token = hashlib.sha256(token.encode()).hexdigest()
    active_tokens = database.check_tokens(user_id)

    if active_tokens:
        for hash_i in active_tokens:
            if hash_i == hash_token:
                return True    
        return False
    
    else:
        return False