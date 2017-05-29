import util.regexes as regexes
from server.entities.request import *
from util.constants.const_main import *
from util.newline import get_newline_char

new_line = CRLF


def transform_request(raw_request):
    global new_line
    new_line = get_newline_char(raw_request)  # Some clients send requests with \r\n, some with \n

    request_lines = raw_request.split(new_line)
    status_line = request_lines[0]
    rest = request_lines[1:]

    headers, body = EMPTY_BYTE_STR, EMPTY_BYTE_STR
    if has_headers(rest) and has_body(rest):
        headers_end = rest.index(EMPTY_BYTE_STR)
        headers_as_list = rest[:headers_end]

        body = CRLF_BYTE.join(rest[headers_end + 1:])
        headers = headers_to_dict(headers_as_list)
    elif has_headers(rest):
        headers = headers_to_dict(rest)

    request_line = parse_status_line(status_line)

    return Request(
        request_line[METHOD],
        request_line[TARGET],
        request_line[QUERY],
        request_line[PROTOCOL],
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


def parse_status_line(status_line):
    found = re.findall(regexes.get_request_regex(), status_line)
    found = found[0]
    if len(found) <= 0: return None
    full, method, target, query, protocol = found
    return {
        METHOD: method,
        TARGET: target,
        QUERY: query,
        PROTOCOL: protocol
    }


def has_headers(request_lines):
    return len(request_lines) >= 1


def has_body(request_lines):
    return EMPTY_BYTE_STR in request_lines