from util.constants.headers import *
from util.constants.const_main import *
from .multipart import get_multipart_fields
from .url_encoded import parse_url_encoded


def decode_body(request):
    if is_multipart(request):
        multipart_fields = get_multipart_fields(request)
        return parse_multipart(multipart_fields)
    else:
        return parse_url_encoded(request.body)


def parse_multipart(multipart_fields):
    fields = {}

    for field in multipart_fields:
        field_name = field.field_name.decode()
        field_value = field.body
        fields[field_name] = field_value

    return fields


def is_multipart(request):
    headers = request.headers
    if has_content_type(request) and MULTIPART in headers[CONTENT_TYPE]:
        return True
    return False


def has_content_type(request):
    return request.headers.__contains__(CONTENT_TYPE)