from storage.entities.publication import Publication
from collections import OrderedDict

_publications = OrderedDict()


def create_publication(username, title, text, attachments=None, _id=None):
    publication = Publication(username, title, text, attachments)
    _id = publication.get_id()
    _publications[_id] = publication
    return publication


def get_publication(unique_id):
    if unique_id in _publications.keys():
        return _publications[unique_id]
    return None


def delete_publication(unique_id):
    if unique_id in _publications.keys():
        del _publications[unique_id]


def get_all_publications():
    for key in reversed(_publications):
        yield _publications[key]