from util.constants.headers import *
from util.regexes import get_session_regex
import re


class Request:
    def __init__(self, method, target, query, protocol, headers=None, body=None):
        self.method = method
        self.target = target
        self.query = query
        self.protocol = protocol
        self.headers = headers
        self.body = body
        self.session = None

    def get_connection(self):
        if CONNECTION in self.headers:
            return self.headers[CONNECTION]

    def get_session_id(self):
        if self.session:
            return self.session.decode()
        elif COOKIE in self.headers:
            cookie = self.headers[COOKIE]
            found = re.findall(get_session_regex(), cookie)
            found = found[0] if found else None
            self.session = found
            return self.session.decode()
