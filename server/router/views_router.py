from paths import *
from storage.publications import PublicationsMemoryDAO
from storage.users import UsersDAO
from storage.sessions import SessionsDAO
from template.compiled_templates import *
from template.template import Template
from util.files import retrieve_file, retrieve_file_buffered


def get_response_file(path, session):
    if is_html(path):
        if is_index(path):
            return build_index(session)
        elif is_publication(path):
            publ_id = get_publication_id(path)
            return build_publication_page(publ_id, session)
        else:
            return retrieve_file_buffered(path)

    else:
        return retrieve_file_buffered(path)


def build_index(session_id):
    data = PublicationsMemoryDAO.get_all_publication()

    html = index_template.render({
        "posts": data,
        "edit_post_url": "/edit", #  TODO edit page
        "user": get_user(session_id)
    })

    return html.encode()


def build_publication_page(publication_id, session_id):
    publication = PublicationsMemoryDAO.get_publication(publication_id)

    html = publication_template.render({
        "publication": publication,
        "user": get_user(session_id),
        "edit_post_url": "/edit"
        # TODO EDIT PAGE
    })

    return html.encode()


def is_html(path):
    return path.endswith('.html')


def is_index(path):
    return path.endswith(INDEX_PAGE)


def is_publication(path): # TODO regex
    return "publication" in path


def get_user(session_id):
    session = SessionsDAO.get_session(session_id)
    session_alive = session.is_alive() if session else False
    return UsersDAO.get_user(session.username) if session_alive else None


def get_publication_id(path):
    return path.split('/')[-1].strip('.html')  # TODO да не, так нельзя