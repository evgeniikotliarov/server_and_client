from storage.publications import PublicationsMemoryDAO
from storage.sessions import SessionsMemoryDAO
from storage.users import UsersMemoryDAO

from template_engine.compiled_templates import index_template, publication_template, profile_template
import template_engine.base_view as base

from util.path import get_public_path, get_component_path, file_exists
from util.files import get_file_type
from util.constants.misc import DEFAULT_CACHE_CONTROL
import util.constants.response_codes as codes
from util.files import retrieve_file_buffered, retrieve_file


# TODO DRY


def get_index(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    file_path = get_component_path(path)
    data = list(PublicationsMemoryDAO.get_all_publications())
    user = get_user(session_id)
    content = index_template.render({
        "user" : user,
        "publications": data,
    })
    base.insert_content(content)
    html = base.render_base({"user": get_user(session_id)})
    mime = get_file_type(file_path)
    response_builder = set_ok(response_builder)
    response_builder = attach_file(response_builder, html, mime)
    return response_builder


def get_publication(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    file_path = get_component_path(path)
    publication_id = query.decode().split('=')[1] # TODO нормально спарсить
    publication = PublicationsMemoryDAO.get_publication(publication_id)
    content = publication_template.render({
        "publication": publication,
        "user": get_user(session_id),
        "edit_post_url": "/edit"
        # TODO EDIT PAGE
    })
    base.insert_content(content)
    html = base.render_base({"user": get_user(session_id)})
    mime = get_file_type(file_path)
    response_builder = set_ok(response_builder)
    response_builder = attach_file(response_builder, html, mime)
    return response_builder


def get_profile(request, response_builder):
    path, session_id, query = request.target, request.get_session_id(), request.query
    file_path = get_component_path(path)
    username = query.decode().strip().split('=')[1]  # TODO нормально спарсить
    user = UsersMemoryDAO.get_user(username)
    content = profile_template.render({
        "user" : user,
        "publications": reversed(user.get_publications())
    })
    base.insert_content(content)
    html = base.render_base({"user": get_user(session_id)})
    mime = get_file_type(file_path)
    response_builder = set_ok(response_builder)
    response_builder = attach_file(response_builder, html, mime)
    return response_builder


def get_static(request, response_builder):
    raw_path = request.target
    if not file_exists(get_public_path(raw_path)):
        file_path = get_component_path(raw_path)
        content = retrieve_file(file_path)
        base.insert_content(content)
        html = base.render_base({'user': get_user(request.get_session_id())})
        mime = get_file_type(file_path)
        response_builder = set_ok(response_builder)
        response_builder = attach_file(response_builder, html, mime)
    else:
        file_path = get_public_path(raw_path)
        response_builder = attach_static(response_builder, file_path)
        response_builder = set_ok(response_builder)
    return response_builder


def get_user(session_id):
    session = SessionsMemoryDAO.get_session(session_id)
    session_alive = session.is_alive() if session else False
    return UsersMemoryDAO.get_user(session.username) if session_alive else None


def set_ok(response_builder):
    code, msg = codes.OK
    response_builder.set_code(code)
    response_builder.set_message(msg)
    return response_builder


def attach_static(response_builder, file_path):
    file = retrieve_file_buffered(file_path)
    mime = get_file_type(file_path)
    response_builder.set_cache_control(DEFAULT_CACHE_CONTROL)  # TODO different cache-controls for different MIMES
    return attach_file(response_builder, file, mime)


def attach_file(response_builder, file, mime):
    response_builder.set_body(file)
    response_builder.set_content_length(len(file))
    response_builder.set_cache_control(DEFAULT_CACHE_CONTROL)  # TODO different cache-controls for different MIMES
    response_builder.set_content_type(mime)
    return response_builder