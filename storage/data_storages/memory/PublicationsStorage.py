from collections import OrderedDict
from storage.entities.Publication import Publication

publications = OrderDict()

def create_publication(author, title, text, attachment=None, unique_id=None):
    publication = Publication(author, title, text, attachment)
    unique_id = generate_id()
    publications[unique_id] = publication
    return publication

def get_publication(unique_id):
    if unique_id in publications.keys():
        return publications[unique_id]
    return None

def delete_publication(unique_id):
    if unique_id in publications.keys():
        del publications[unique_id]

