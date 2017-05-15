from storage.publications import *
import util.constants.response_codes as codes
from util.constants.headers import COOKIE

from server.form_encodings.decoder import decode_body
from util.files import *
from util.id_generator import generate_id
from util.strings import ensure_string
from util.constants.paths import *
from util.redirect_generator import redirect_builder


def do_publish(request, response_builder):
    publish_fields = decode_body(request)

    # author = request.headers[COOKIE] TODO parse author via sessions cookie
    title, text, attachment = publish_fields['title'], publish_fields['text'], publish_fields['attachment']
    attachment = save_attachment(attachment)

    title, text, attachment = ensure_string(title, text, attachment)

    PublicationsMemoryDAO.create_publication("Author", title, text, attachment)

    created_code, created_message = codes.CREATED
    response_builder.set_code(created_code)
    response_builder.set_message(created_message)

    response_builder.set_redirect(redirect_builder(INDEX_PAGE))

    return response_builder


def do_delete(request, response_builder):
    _id = decode_body(request.body)["id"]
    PublicationsMemoryDAO.delete_publication(_id)

    code, message = codes.ACCEPTED
    response_builder.set_code(code)
    response_builder.set_message(message)

    response_builder.set_redirect(redirect_builder(INDEX_PAGE))

    return response_builder

def save_attachment(attachment):
    _id = generate_id()
    filename = _id + ".jpg" #  TODO Сделать это нормально
    save_image(attachment, filename, ABS_IMAGES_FOLDER)
    return join(IMAGES_FOLDER, filename)