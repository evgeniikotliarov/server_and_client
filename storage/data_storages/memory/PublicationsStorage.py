import uuid
from storage.entities.Publication import Publication

publications = {}

def create_publication(username, title, text, attachment=None):
    publication = Publication(username, title, text, attachment)
    unique_id = generate_id()
    publications[unique_id] = publication
    return publication

def get_publication(unique_id):
    if unique_id in publications.keys():
        return publications[unique_id]
    return None

def generate_id():
    unique_id = uuid.uuid4()
    return unique_id
    # TODO