class Request:
    def __init__(self, method, target, query, protocol, headers=None, body=None):
        self.method = method
        self.target = target
        self.query = query
        self.protocol = protocol
        self.headers = headers
        self.body = body