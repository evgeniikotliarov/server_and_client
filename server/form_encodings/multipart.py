import re
from util.constants.headers import *
from util.constants.const_main import *
from util.regexes import *

def get_multipart_fields(request):
    multipart_fields = []
    # ---------------------------165903753415996587151253452    - in Content-type
    # -----------------------------165903753415996587151253452  - Actual boundary
    # -----------------------------165903753415996587151253452-- - Last boundary
    boundary_in_header = get_boundary(request)
    boundary = b'--' + boundary_in_header
    boundary_finish = boundary + b'--'

    fields = request.body.split(boundary)

    # First field is always not needed because it contains request headers
    # Last field is always boundary+'--' so it is always split as '--'
    # We can throw them off
    fields = fields[1:-1]

    for field in fields:
        multipart_fields.append(wrap_multipart(field))

    return multipart_fields

def get_boundary(request):
    content_type = request.headers[CONTENT_TYPE]
    reg = get_boundary_regex()
    found = re.search(reg, content_type)
    if found:
        return found.group(1)

def wrap_multipart(multipart_field):
    disposition_regex = get_content_disposition_regex()
    found = re.search(disposition_regex, multipart_field)
    disposition = found.group(1) if found else None

    content_type_regex = get_content_type_regex()
    found = re.search(content_type_regex, multipart_field)
    content_type = found.group(1) if found else None

    file_part_regex = get_multipart_body_regex()
    found = re.search(file_part_regex, multipart_field)
    file_bytes = found.group(1) if found else None

    return MultipartField(disposition, content_type, file_bytes)


class MultipartField:
    def __init__(self, disposition, content_type, body):
        self.field_name = self._get_field_name(disposition)
        self.content_type = content_type
        self.body = body

    @staticmethod
    def _get_field_name(disposition):
        name_regex = get_disposition_name_regex()
        found = re.search(name_regex, disposition)
        name = found.group(1)
        return name