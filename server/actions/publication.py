from paths import *
from server.form_encodings.decoder import decode_body
from storage.publications import *
from util.files import *
from util.id_generator import generate_id
from util.strings import ensure_string
from util.redirect import do_redirect
from storage.sessions import SessionsMemoryDAO
from storage.users import UsersMemoryDAO


def do_publish(request, response_builder):
    publish_fields = decode_body(request)

    session_id = request.get_session_id()
    session = SessionsMemoryDAO.get_session(session_id)
    username = session.username if session else None
    user = UsersMemoryDAO.get_user(username)

    title, text, attachment = publish_fields['title'], publish_fields['text'], publish_fields['attachment']
    attachment = save_attachment(attachment)
    title, text, attachment = ensure_string(title, text, attachment)
    publication = PublicationsMemoryDAO.create_publication(username, title, text, attachment)
    if user: user.add_publication(publication)
    print(user.get_publications())
    return do_redirect(INDEX_PAGE, response_builder)


def do_delete(request, response_builder):
    _id = decode_body(request.body)["id"]
    PublicationsMemoryDAO.delete_publication(_id)

    return do_redirect(INDEX_PAGE, response_builder)


def save_attachment(attachment):
    _id = generate_id()
    filename = _id + ".jpg" #  TODO Сделать это нормально, по майму или спарсить файлнейм из мультипарта
    save_image(attachment, filename, ABS_IMAGES_FOLDER)
    return join(IMAGES_FOLDER, filename)
