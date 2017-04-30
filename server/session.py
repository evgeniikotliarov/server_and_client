import uuid
import time

class Session:
    def __init__(self):
        self.id = None
        self.age = None

    def generate_id(self):
        self.age = time.time()
        self.id = uuid.uuid4()
        return str(self.id)

    def update_age(self):
        self.age = time.time()