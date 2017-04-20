import re
from constants.headers import *
from constants.const_main import MULTIPART, EMPTY_STRING
from util.regexes import get_boundary_regex

'''
    All requests come as instances of server/entities/Request.py class
'''
def get_file_part(request):
    # ---------------------------165903753415996587151253452    - in Content-type
    # -----------------------------165903753415996587151253452  - Actual boundary
    # -----------------------------165903753415996587151253452-- - Last boundary
    if not is_multipart(request): return None
    boundary_in_header = get_boundary(request)
    boundary = '--' + boundary_in_header
    boundary_finish = boundary + '--'

    split_by_boundary = request.body.split(boundary)

    return True # Just for running it in tests

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

class MultipartRequest:
    def __init__(self):
        pass