def do_error(error, request, response_builder):
    code, message = error
    response_builder.set_code(code)
    response_builder.set.message(message)

    return response_builder