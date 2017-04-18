from constants.headers import *

class HeaderHandler:

    def __init__(self, headers):
        self._headers = headers
        self._params = None

    def make_params(self):
        accept_val = self._headers[ACCEPT]
        accept = self.handle_accept(accept_val)

        accept_charset_val = self._headers[ACCEPT_CHARSET]
        accept_charset = self.handle_accept_charset(accept_charset_val)

        accept_encoding_val = self._headers[ACCEPT_ENCODING]
        accept_encoding = self.handle_accept_encoding(accept_encoding_val)

        accept_language_val = self._headers[ACCEPT_LANGUAGE]
        accept_language = self.handle_accept_language(accept_language_val)

        cache_control_val = self._headers[CACHE_CONTROL]
        cache_control = self.handle_cache_control(cache_control_val)

        connection_val = self._headers[CONNECTION]
        connection = self.handle_connection(connection_val)

        cookie_val = self._headers[COOKIE]
        cookie = self.handle_cookie(cookie_val)

        content_length_val = self._headers[CONTENT_LENGTH]
        content_length = self.handle_content_length(content_length_val)

        content_type_val = self._headers[CONTENT_TYPE]
        content_type = self.handle_content_type(content_type_val)

        date_val = self._headers[DATE]
        date = self.handle_date(date_val)

        expect_val =self._headers[EXPECT]
        expect = self.handle_expect(expect_val)

        from_val = self._headers[FROM]
        from_val = self.handle_from(from_val)

        host_val = self._headers[HOST]
        host = self.handle_host(host_val)

        if_match_val = self._headers[IF_MATCH]
        if_match = self.handle_if_match(if_match_val)

        if_modified_since_val = self._headers[IF_MODIFIED_SINCE]
        if_modified_since = self.handle_if_modified_since(if_modified_since_val)

        if_none_macth_val = self._headers[IF_NONE_MATCH]
        if_none_match = self.handle_if_none_match(if_none_macth_val)

        if_range_val = self._headers[IF_RANGE]
        if_range = self.handle_if_range(if_range_val)

        range_val = self._headers[RANGE]
        range = self.handle_range(range_val)

        referer_val = self._headers[REFERER]
        referer = self.handle_referer(referer_val)

        user_agent_val = self._headers[USER_AGENT]
        user_agent = self.handle_user_agent(user_agent_val)

        upgrade_val = self._headers[UPGRADE]
        upgrade = self.handle_upgrade(upgrade_val)

    def handle_accept(self, value):
        return value


    def handle_accept_charset(self, value):
        return  value

    def handle_accept_encoding(self, value):
        return value

    def handle_accept_language(self, value):
        return  value

    def handle_accept_datetime(self, value):
        return value

    def handle_cache_control(self, value):
        return value

    def handle_connection(self, value):
        return value

    def handle_cookie(self, value):
        return value

    def handle_content_length(self, value):
        return value

    def handle_content_type(self, value):
        return value

    def handle_date(self, value):
        return value

    def handle_expect(self, value):
        return value

    def handle_from(self, value):
        return value

    def handle_host(self, value):
        return value

    def handle_if_match(self, value):
        return value

    def handle_if_modified_since(self, value):
        return value

    def handle_if_none_match(self, value):
        return value

    def handle_if_range(self, value):
        return value

    def handle_range(self, value):
        return value

    def handle_referer(self, value):
        return value

    def handle_user_agent(self, value):
        return value

    def handle_upgrade(self, value):
        return value
