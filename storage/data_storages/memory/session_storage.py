from storage.entities.session import Session

_sessions = {}

def create_sessions(username, age):
    session = Session(username, age)
    _sessions[session.get_id()] = session
    return session.get_id

def get_session(_id):
    return _sessions[_id] if _id in _sessions else None

def delete_session(_id):
    if _id in _sessions:
        del _sessions[_id]

