import time
from util.id_generator import generate_id


class Session:
    def __init__(self, username, max_age):
        self._id = generate_id()
        self.username = username
        self.born = self.refresh()
        self.max_age = max_age

    def is_alive(self):
        now = time.time()
        if now - self.born > self.max_age:
            return False
        else:
            self.refresh()
            return True

    def get_id(self):
        return self._id

    def refresh(self):
        self.born = time.time()
        return self.born

