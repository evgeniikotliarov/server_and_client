from util.constants.response_codes import SEE_OTHER

def do_redirect(page, response_builder):
    code, message = SEE_OTHER
    response_builder.set_code(code)
    response_builder.set_message(message)
    response_builder.set_location(page.encode())
    return response_builder
