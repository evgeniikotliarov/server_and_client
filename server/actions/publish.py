from server.form_encodigs import multipart

def do_publish():
    pass


def publish(multipart_fields):
    author = None

def parser_fields(multipart_fields):

    dict_parser_multipart_fields = {}

    for field in multipart_fields:
        name = field.field_name
        if name == 'title':
            form_name = field.body
            dict_parser_multipart_fields['name'] = form_name
        if name == 'text':
            form_text = field.body
            dict_parser_multipart_fields['text'] = form_text
        if name == 'attachments':
            form_attachments = field.body
            dict_parser_multipart_fields['attachments'] = form_attachments

    return dict_parser_multipart_fields