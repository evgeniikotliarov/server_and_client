import util.constants.response_codes as codes

def head_index(request, response_builder):
    return set_ok(response_builder)


def head_publication(request, response_builder):
    return set_ok(response_builder)


def head_userpage(request, response_builder):
    return set_ok(response_builder)


def head_static(request, response_builder):
    return set_ok(response_builder)

def set_ok(response_builder):
    code, msg = codes.OK
    response_builder.set_code(code)
    response_builder.set_message(msg)
    return response_builder