from server.form_encodings.multipart import get_multipart_fields
from storage.publications import *
import util.constants.response_codes as codes

from util.files import *
from util.id_generator import generate_id
from util.strings import ensure_string


def do_publish(request, response_builder):
    multipart_fields = get_multipart_fields(request)
    publish_fields = parser_fields(multipart_fields)

    title = publish_fields['title']
    text = publish_fields['text']
    att = publish_fields['attachment']

    title, text, att = ensure_string(title, text, att)

    PublicationsDAO.create_publication("Author", title, text, att)

    created_code, created_message = codes.CREATED
    response_builder.set_code(created_code)
    response_builder.set_message(created_message)

    return response_builder


def parser_fields(multipart_fields):
    dict_parser_multipart_fields = {}

    for field in multipart_fields:
        name = field.field_name
        if name == b'title':
            form_name = field.body
            dict_parser_multipart_fields['title'] = form_name
        if name == b'text':
            form_text = field.body
            dict_parser_multipart_fields['text'] = form_text
        if b'attachment' in name:
            form_attachment = field.body
            _id = generate_id()
            filename = (str(_id) + ".jpg")
            save_image(form_attachment, filename)
            dict_parser_multipart_fields['attachment'] = 'image/' + _id + ".jpg"

    return dict_parser_multipart_fields