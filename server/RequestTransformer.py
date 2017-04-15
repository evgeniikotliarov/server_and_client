from server.entities.Request import *
import re
from constants.const_main import *



def proceed_request(request_data):
    request_data_line = request_data.split(NEWLINE)

    headers = ""
    body = ""

    request_line_text = request_data_line[0]
    if len(request_data_line) > 1:
        headers_and_body = request_data_line[:1]
        body_and_headers_divider = headers_and_body.index(EMPTY_STRING)
        headers_as_string = headers_and_body[:body_and_headers_divider]
        body = headers_and_body[body_and_headers_divider + 1:]
        headers = headers_to_dict(headers_as_string)

    request_line = parse_request_line(request_line_text)

    request = Request(\
        request_line["method"],\
        request_line["target"],\
        request_line["query"],\
        request_line["protocol"],\
        headers,\
        body)
    return request
def headers_to_dict(headers_list):
    headers = {}
    for header in headers_list:
        name, value = header.split(":", 1)
        name, value = name.strip(), value.strip()
        headers[name] = value
    return headers
