from constants.headers import *
class HeaderHandler:
    def __init__(self, headers):
        self._headers = headers
        self._params = None

    def make_params(self):
        accept_val = self._headers[ACCEPT]
        accept = self.handle_accept(accept_value)

        accept_charset_val = self._headers[ACCEPT_CHARSET]

    def handle_accept(self, value):
        return value
