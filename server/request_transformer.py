import re

import util.regexes as Regexes
from storage.entities.request import *
from util.constants.const_main import *
from util.newline import get_newline_char

new_line = CRLF

def transform_request(raw_request):
    global new_line
    new_line = get_newline_char(raw_request)

    request_lines = raw_request.split(new_line)
    if len(request_lines[0]) < 1:
        request_lines = request_lines[1:]

    request_line_text = request_lines[0]
    rest = request_lines[1:]

    headers, body = b'', b''
    if has_headers(rest) and has_body(rest):
        headers_end = rest.index(EMPTY_BYTE_STR)
        headers_as_list = rest[:headers_end]

        body = CRLF_BYTE.join(rest[headers_end + 1:])
        headers = headers_to_dict(headers_as_list)
    elif has_headers(rest):
        headers = headers_to_dict(rest)

    request_line = parse_request_line(request_line_text)

    return Request(
        request_line["method"],
        request_line["target"],
        request_line["query"],
        request_line["protocol"],
        headers,
        body)

def headers_to_dict(headers_list):
    headers = {}
    for header in headers_list:
        if BYTE_COLON not in header:
            continue
        name, value = header.split(BYTE_COLON, 1)
        name, value = name.strip(), value.strip()
        headers[name] = value
    return headers

def parse_request_line(request):
    found = re.findall(Regexes.get_request_regex(), request)
    found = found[0]
    if len(found) <= 0: return None
    full, method, target, query, protocol = found
    return {
        'method': method,
        'target': target,
        'query': query,
        'protocol': protocol
    }

def has_headers(request_lines):
    return len(request_lines) >= 1

def has_body(request_lines):
    return EMPTY_BYTE_STR in request_lines