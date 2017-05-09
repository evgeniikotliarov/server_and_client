import time
from util.id_generator import generate_id


class Session:
    def __init__(self, username, age):
        self.id = generate_id()
        self.username = username
        self.age = age
        self.born = self.update_born

    def update_born(self):
        self.born = time.time()
        return self.born