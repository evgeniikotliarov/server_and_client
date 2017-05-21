from storage.publications import PublicationsMemoryDAO
from storage.sessions import SessionsMemoryDAO
from storage.users import UsersMemoryDAO

from template.compiled_templates import index_template
from util.path import get_filesystem_path
from util.files import get_file_type
from util.constants.const_main import DEFAULT_CACHE_CONTROL
import util.constants.response_codes as codes

def serve_index(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    file_path = get_filesystem_path(path)
    data = PublicationsMemoryDAO.get_all_publications()
    html = index_template.render({
        "posts": data,
        "edit_post_url": "/edit", #TODO edit page
        "user": get_user(session_id)
    }).encode()

    mime = get_filesystem_path(file_path)

    code, msg = codes.OK
    response_builder.set_code(code)
    response_builder.set_message(msg)
    response_builder.set_body(html)
    response_builder.set_content_length(len(html))
    response_builder.set_content_type(mime)
    response_builder.set_cache_control(DEFAULT_CACHE_CONTROL) #TODO different cache-control for different
    return response_builder

def serve_publication(request, response_builder):
    pass

def serve_userpage(request, response_builder):
    pass

def get_user(session_id):
    session = SessionsMemoryDAO.get_session(session_id)
    session_alive = session.is_alive() if session else False
    return  UsersMemoryDAO.get_user(session.username) if session_alive else None