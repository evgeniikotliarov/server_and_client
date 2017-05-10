from storage.entities.session import Session
from util.id_generator import generate_id

sessions = {}

def create_sessions(username, age):
    session = Session(username, age)
    session.set_id(generate_id())
    return session.id