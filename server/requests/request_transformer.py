import util.regexes as regexes
from server.entities.request import *
from util.constants.const_main import *
from util.newline import get_newline_char
from aliases import ALIASES
new_line = CRLF


class RequestTransformer:
    def __init__(self, request):
        self.raw_request = request

    def transform(self):
        global new_line
        new_line = get_newline_char(self.raw_request)

        request_lines = self.raw_request.split(new_line)
        status_line = request_lines[0]
        rest = request_lines[1:]

        headers, body = EMPTY_BYTE_STR, EMPTY_BYTE_STR
        if self.has_headers(rest) and self.has_body(rest):
            headers_end = rest.index(EMPTY_BYTE_STR)
            headers_as_list = rest[:headers_end]

            body = CRLF_BYTE.join(rest[headers_end + 1:])
            headers = self.headers_to_dict(headers_as_list)
        elif self.has_headers(rest):
            headers = self.headers_to_dict(rest)

        request_line = self.parse_status_line(status_line)

        request = Request(
            request_line["method"],
            request_line["target"],
            request_line["query"],
            request_line["protocol"],
            headers,
            body)

        return self.insert_aliases(request)

    @staticmethod
    def headers_to_dict(headers_list):
        headers = {}
        for header in headers_list:
            if BYTE_COLON not in header:
                continue
            name, value = header.split(BYTE_COLON, 1)
            name, value = name.strip(), value.strip()
            headers[name] = value
        return headers

    @staticmethod
    def parse_status_line(status_line):
        found = re.findall(regexes.get_request_regex(), status_line)
        found = found[0]
        if len(found) <= 0: return None
        full, method, target, query, protocol = found
        return {
            'method': method,
            'target': target,
            'query': query,
            'protocol': protocol
        }

    @staticmethod
    def has_headers(request_lines):
        return len(request_lines) >= 1

    @staticmethod
    def has_body(request_lines):
        return EMPTY_BYTE_STR in request_lines

    @staticmethod
    def insert_aliases(request):
        if request.target in ALIASES:
            request.target = ALIASES[request.target]
        return request