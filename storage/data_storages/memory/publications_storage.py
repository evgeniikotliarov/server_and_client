from collections import OrderedDict
from storage.entities.publication import Publication
from util.id_generator import generate_id

_publications = OrderedDict()

def create_publication(author, title, text, attachment=None, unique_id=None):
    publication = Publication(author, title, text, attachment)
    unique_id = generate_id()
    _publications[unique_id] = publication
    return publication

def get_publication(unique_id):
    if unique_id in _publications.keys():
        return _publications[unique_id]
    return None

def delete_publication(unique_id):
    if unique_id in _publications.keys():
        del _publications[unique_id]

def get_all_publication():
    for value in _publications.values():
        yield value
