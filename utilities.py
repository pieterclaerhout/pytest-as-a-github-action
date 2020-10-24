import uuid

def create_uuid():
    return str(uuid.uuid1()).replace('-', '').lower()
