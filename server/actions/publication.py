from storage.publications_dao_factory import PublicationsDAOFactory
from storage.sessions_dao_factory import SessionsDAOFactory
from storage.users_dao_factory import UsersDAOFactory

from paths import *
from server.form_encodings.decoder import decode_body
from util.files import *
from util.id_generator import generate_id
from util.redirect import do_redirect
from util.strings import ensure_string
from util.constants.const_main import IN_MEMORY


def do_publish(request, response_builder, _id=None):
    publish_fields = decode_body(request)

    session_id = request.get_session_id()
    session = SessionsDAOFactory.get_storage(IN_MEMORY).get_session(session_id)
    username = session.username if session else None
    user = UsersDAOFactory.get_storage(IN_MEMORY).get_user(username)

    title, text = publish_fields['title'], publish_fields['text']
    attachments = get_attachments(publish_fields)
    attachments_paths = save_attachments(attachments)
    title, text = ensure_string(title, text)

    if _id:
        publication = PublicationsDAOFactory.get_storage(IN_MEMORY).\
            create_publication(username, title, text, attachments_paths, _id=_id)
    else:
        publication = PublicationsDAOFactory.get_storage(IN_MEMORY)\
            .create_publication(username, title, text, attachments_paths)
    if user and not _id:
        user.add_publication(publication)
    return do_redirect(INDEX_PAGE, response_builder)


def do_edit(request, response_builder):
    post_id = request.query.decode().split('=')[1]  # TODO спарсить нормально
    old_post = PublicationsDAOFactory.get_storage(IN_MEMORY)\
        .get_publication(post_id)
    PublicationsDAOFactory.get_storage(IN_MEMORY)\
        .delete_publication(post_id)
    do_publish(request, response_builder, post_id)

    author = UsersDAOFactory.get_storage(IN_MEMORY).get_user(old_post.author)
    author_publications = author.publications
    index = author_publications.index(old_post)
    author_publications[index] = PublicationsDAOFactory.get_storage(IN_MEMORY).get_publication(post_id)

    return do_redirect(INDEX_PAGE, response_builder)


def do_delete(request, response_builder):
    _id = request.query.decode().split("=")[1]
    publication = PublicationsDAOFactory.get_storage(IN_MEMORY)\
        .get_publication(_id)
    author = UsersDAOFactory.get_storage(IN_MEMORY).get_user(publication.author)
    if publication in author.publications:
        author.publications.remove(publication)
        PublicationsDAOFactory.get_storage(IN_MEMORY).delete_publication(_id)

    return do_redirect(INDEX_PAGE, response_builder)


def get_attachments(fields):
    attachments = []
    for field, value in fields.items():
        if field.startswith('attachment') and value:
            attachments.append(value)
    return attachments


def save_attachments(attachments):
    paths = []
    for att in attachments:
        _id = generate_id()
        filename = _id + ".jpg" #  TODO Сделать это нормально, по майму или спарсить файлнейм из мультипарта
        save_image(att, filename, UPLOADS_ABS_FOLDER)
        paths.append(join(UPLOADS_FOLDER, filename))
    return paths