class Response:
    def __init__(self, code, message, protocol, headers, body):
        self.code = code
        self.message = message
        self.protocol = protocol
        self.headers = headers
        self.body = body
