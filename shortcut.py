from config import RZN_TYPES

def get_type_title(type_id):
    global RZN_TYPES
    for type_ in RZN_TYPES:
        if type_[0] == type_id:
            return type_[1]
    return False