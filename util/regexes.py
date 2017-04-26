def get_request_regex():
    methods = r'GET|POST|PUT|DELETE|OPTIONS'
    host_symbols = r'[\w.\-\d/:]'
    space = r'\s'
    query = r'(?:[?&][^\s&]+)*'
    protocol = r'HTTP/.*'
    request_regex = "(({methods}){space}+({host_symbols}+)({query}){space}+({protocol}))".format(
        methods = methods,
        space = space,
        host_symbols = host_symbols,
        query = query,
        protocol = protocol
        )
    return request_regex.encode()

def get_boundary_regex():
    return b'boundary=(.+)'

def get_content_disposition_regex():
    r = br'Content-Disposition:\s?(.*)\r\n'
    return r

def get_content_type_regex():
    r = br'Content-Type:\s?(.*)\r\n'
    return r

def get_multipart_body_regex():
    r = br'Content-Disposition:\s?.*(?:[\r\n]{0,1}Content-Type:\s?.*[\r\n]{0,1})?.*[\r\n]*(.*)\r?'
    return r