from server.form_encodigs.multipart import get_multipart_fields
from storage.publications import *
import util.constants.response_codes as codes


def do_publish(request, response_builder):
    multipart_fields = get_multipart_fields(request)
    publish_fields = parser_fields(multipart_fields)
    PublicationsDAO.create_publication(publish_fields)

    created_code, created_message = codes.CREATED
    response_builder.set_code(created_code)
    response_builder.set_message(created_message)

    return response_builder


def publish(multipart_fields):
    author = None


def parser_fields(multipart_fields):
    dict_parser_multipart_fields = {}

    for field in multipart_fields:
        name = field.field_name
        if name == 'title':
            form_name = field.body
            dict_parser_multipart_fields['title'] = form_name
        if name == 'text':
            form_text = field.body
            dict_parser_multipart_fields['text'] = form_text
        if name == 'attachment':
            form_attachment = field.body
            dict_parser_multipart_fields['attachment'] = form_attachment

    return dict_parser_multipart_fields