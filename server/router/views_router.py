from paths import *
from storage.publications import PublicationsMemoryDAO
from storage.users import UsersDAO
from storage.sessions import SessionsDAO
from template.compiled_templates import index_template
from template.template import Template
from util.files import retrieve_file, retrieve_file_buffered


def get_response_files(path, session):
    if isHtml(path):
        if isIndex(path):
            return build_index(session)

    elif 'post' in path and 'create' not in path: #TODO можно переделать это
        _id = path.split('/')[-1]
        publication = PublicationsMemoryDAO.get_publication(_id)
        html_data = retrieve_file(path)
        template = Template(html_data)
        template.compile()
        template.render({
            "post": publication
        })

    else:
        return retrieve_file_buffered(path)


def build_index(session_id):
    data = PublicationsMemoryDAO.get_all_publication()

    html = index_template.render({
        "post": data,
        "edit_post_utl": "/edit",
        "post_url": "/publication",
        "user":get_user(session_id)
    })

    return html.encode()


def isHtml(path):
    return path.endswith('.html')


def isIndex(path):
    return path.endswith(INDEX_PAGE)


def get_user(session_id):
    session = SessionsDAO.get_session(session_id)
    session_alive = session.is_alive() if session else False
    return UsersDAO.get_user(session.username) if session_alive else None