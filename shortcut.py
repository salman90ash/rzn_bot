from config import RZN_TYPES_add


def get_type_title(type_id):
    global RZN_TYPES_add
    for type_ in RZN_TYPES_add:
        if type_[0] == type_id:
            return type_[1]
    return False