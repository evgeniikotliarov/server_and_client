import re

from server.entities.Request import *
from constants.const_main import *
from util.newline import get_newline_char
import util.regexes as Regexes

def proceed_request(raw_request):
    new_line = get_newline_char(raw_request)
    request_data_lines = raw_request.split(new_line)
    if len(request_data_lines[0]) < 1:
        request_data_lines = request_data_lines[1:]

    headers = ""
    body = ""

    request_line_text = request_data_lines[0]
    if len(request_data_lines) > 1:
        headers_and_body = request_data_lines[1:]
        body_and_header_divider = headers_and_body.index(EMPTY_STRING)
        headers_as_strings = headers_and_body[:body_and_header_divider]
        body = headers_and_body[body_and_header_divider + 1:]
        headers = headers_to_dict(headers_as_strings)

    request_line = parse_request_line(request_line_text)

    request = Request(
        request_line["method"],
        request_line["target"],
        request_line["query"],
        request_line["protocol"],
        headers,
        body)

    return request

def headers_to_dict(headers_list):
    headers = {}
    for header in headers_list:
        name, value = header.split(":", 1)
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