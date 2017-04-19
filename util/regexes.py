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
    return request_regex

def get_boundary_regex():
    return 'boundary=(.+)'