from storage.sessions import *


sessions = {}

def create_sessions(session_id, username):
    session = Session(session_id, username)
    ses = session_id
    return session_id