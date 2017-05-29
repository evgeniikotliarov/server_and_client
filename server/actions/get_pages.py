from storage.publications import PublicationsMemoryDAO
from storage.sessions import SessionsMemoryDAO
from storage.users import UsersMemoryDAO

from template.compiled_templates import index_template, publication_template, profile_template, edit_page_template
import template.base_view as base

from util.path import get_public_path, get_component_path, file_exists
from util.files import get_file_type
from util.constants.const_main import DEFAULT_CACHE_CONTROL
import util.constants.response_codes as codes
from util.files import retrieve_file_buffered, retrieve_file

#TODO refractor


def get_index(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    publications = list(PublicationsMemoryDAO.get_all_publications())
    data = {"publications": publications}
    page = build_html(index_template, data, session_id)
    mime = get_file_type(get_component_path(path))
    response_builder = attach_file_and_headers(response_builder, page, mime)
    return set_ok(response_builder)


def get_publication(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    _id = query.decode().split('=')[1]  # TODO нормально спарсить
    publication = PublicationsMemoryDAO.get_publication(_id)
    is_author = (SessionsMemoryDAO.get_session(session_id).username == publication.author)
    data = {
        "publication": publication,
        "is_author": is_author
    }
    page = build_html(publication_template, data, session_id)
    mime = get_file_type(get_component_path(path))
    response_builder = attach_file_and_headers(response_builder, page, mime)
    return set_ok(response_builder)


def get_edit_post(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    publication_id = query.decode().split('=')[1]
    publication = PublicationsMemoryDAO.get_publication(publication_id)
    data = {"publication": publication}
    page = build_html(edit_page_template, data, session_id)
    mime = get_file_type(get_component_path(path))
    response_builder = attach_file_and_headers(response_builder, page, mime)
    return set_ok(response_builder)


def get_profile(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    username = query.decode().strip().split('=')[1]  # TODO нормально спарсить
    user = UsersMemoryDAO.get_user(username)
    data = {"publications": reversed(user.get_publications())}
    page = build_html(profile_template, data, session_id)
    mime = get_file_type(get_component_path(path))
    response_builder = attach_file_and_headers(response_builder, page, mime)
    return set_ok(response_builder)


def get_static(request, response_builder):
    raw_path = request.target
    if is_component(raw_path):
        file_path = get_component_path(raw_path)
        base.insert_content(retrieve_file(file_path))
        page = base.render_base({'user': get_user(request.get_session_id())})
    else:
        file_path = get_public_path(raw_path)
        page = retrieve_file_buffered(file_path)

    mime = get_file_type(file_path)
    response_builder = attach_file_and_headers(response_builder, page, mime)
    return set_ok(response_builder)


def build_html(template, data, session_id):
    content = template.render(data)
    base.insert_content(content)
    html = base.render_base({"user": get_user(session_id)})
    return html


def get_user(session_id):
    session = SessionsMemoryDAO.get_session(session_id)
    session_alive = session.is_alive() if session else False
    return UsersMemoryDAO.get_user(session.username) if session_alive else None


def set_ok(response_builder):
    code, msg = codes.OK
    response_builder.set_code(code)
    response_builder.set_message(msg)
    return response_builder


def attach_file_and_headers(response_builder, file, mime):
    response_builder.set_body(file)
    response_builder.set_content_length(len(file))
    response_builder.set_cache_control(DEFAULT_CACHE_CONTROL)  # TODO different cache-controls for different MIMES
    response_builder.set_content_type(mime)
    return response_builder


def is_component(raw_path):
    return not file_exists(get_public_path(raw_path)) and get_component_path(raw_path)