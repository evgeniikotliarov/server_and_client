from util.constants.response_codes import SEE_OTHER, OK

def do_redirect(page, response_builder):
    code, message = SEE_OTHER
    response_builder.set_code(code)
    response_builder.set_message(message)
    response_builder.set_location(page.encode())
    return response_builder


def wrong_credentials(response_builder):
    return  _send_text("<h1>Wrong credentials.</h1>", response_builder)


def user_exists(response_builder):
    return _send_text("<h1>This username already exists</h1>", response_builder)


def _send_text(text, response_builder):
    code, message = OK
    response_builder.set_code(code)
    response_builder.set_message(message)
    response_builder.set_body(text.encode())
    return response_builder