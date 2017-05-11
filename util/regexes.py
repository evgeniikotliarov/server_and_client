def get_regex_date_format():
    return r'\w{3},\s\d{2}\s\w{3}\s\d{4}\s\d{2}:\d{2}:\d{2}\s[A-Z]{3}'

def get_request_regex():
    methods = r'\w+'
    host_symbols = r"[\w\.\-\d/:'0-9]"
    space = r'\s'
    query = r'(?:[?&][^\s&]+)*'
    protocol = r'HTTP/.*'
    request_regex = "(({methods}){space}+({host_symbols}+)({query}){space}+({protocol}))".format(
        methods=methods,
        space=space,
        host_symbols=host_symbols,
        query=query,
        protocol=protocol
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
    r = br'Content-Disposition:\s?.*(?:[\r\n]{0,1}Content-Type:\s?.*[\r\n]{0,1})?.*[\r\n]*([\s\S]*)'
    return r

def get_disposition_name_regex():
    r = br'name="(.*)"'
    return r
