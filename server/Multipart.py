import re
from constants.headers import *
from constants.const_main import *
from util.regexes import *

'''
    All requests come as instances of server/entities/Request.py class
'''
def get_file_part(request):
    # ---------------------------165903753415996587151253452    - in Content-type
    # -----------------------------165903753415996587151253452  - Actual boundary
    # -----------------------------165903753415996587151253452-- - Last boundary
    if not is_multipart(request): return None
    boundary_in_header = get_boundary(request)
    boundary = b'--' + boundary_in_header
    boundary_finish = boundary + b'--'

    fields = request.body.split(boundary)

    # First field is always not needed because it contains request headers
    # Last field is always boundary+'--' so it is always split as '--'
    # We can throw them off
    fields = fields[1:-1]

    return True # TODO remove this - just for running it in tests

def if_multipart(request):
    headers = request.headers
        if has_content_type(request) and MULTIPART in headers[CONTENT_TYPE]:
            return True
        return False
def get_boundary(request):
    if is_multipart(request):
        content_type = request.headers[CONTENT_TYPE]
        reg = get_boundary_regex()
        found = re.search(reg, content_type)
        if found:
            return found.group(1)
    return None

def has_content_type(request):
    return request.headers.__constants__(CONTENT_TYPE)

def wrap_multipart(multipart_field):
    disposition_regex = get_content_disposition_regex()
    found = re.search(disposition_regex, multipart_field)
    disposition = found.group(1) if found else None

    content_type_regex = get_content_type_regex()
    found = re.search(content_type_regex, multipart_field)
    content_type = found.group(1) if found else None

    file_part_regex = get_multipart_file_regex()
    found = re.search(file_part_regex, multipart_field)
    file_bytes = found.group(1) if found else None

    return MultipartRequest(disposition, content_type, file_bytes)

class MultipartRequest:
    def __init__(self, disposition, content_type, file):
        self.content_disposition = disposition
        self.content_type = content_type
        self.file = file


class MultipartRequest:
    def __init__(self):
        pass