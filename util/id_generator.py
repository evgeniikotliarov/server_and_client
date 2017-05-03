from uuid import uuid4

def generate_etag():
    return str(uuid4()).encode()

def generate_id():
    return str(uuid4()).encode()