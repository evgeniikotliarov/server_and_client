from datetime import datetime, tzinfo, timedelta

class ResponseBuilder:

    def get_allow(self):
        allow = "Allow: GET, POST, PUT, DELETE, OPTIONS"
        return allow

    def get_cache_control(self):
        cache_control = "Cache-control: max-age=3600"
        return cache_control

    def get_connection(self):
        connection = "Connection: close"
        return connection

    def get_content_encoding(self):
        content_encoding = "Content-Encoding: gzip"
        return content_encoding

    def get_content_language(self):
        content_language = "Content-Language: ru, en"
        return content_language

    def get_content_length(self):
        content_length = "Content-Length: 3495"
        return content_length

    def get_date(self):
        date = datetime.now(GMT1())
        date_return = date.strftime("%a, %d %b %Y %H:%M:%S %Z")
        return date_return

    def get_e_tag(self):
        return ""

    def get_last_modified(self):
        last_modified = self.get_date()
        return last_modified

    def get_expires(self):
        expires = self.get_date()
        return expires

    def get_location(self):
        return ""

    def get_server(self):
        server = "My server"
        return server

    def set_cookie(self):
        return ""

    def get_status(self):
        return ""

class GMT1(tzinfo):

    def utcoffset(self, dt):
        return timedelta(hours = 0)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self,dt):
        return "GMT"