import util.constants.response_codes as codes


def do_head(request, response_builder):
    ok_code, ok_message = codes.OK
    connection = request.get_connection()  # TODO сделать нормально keep-alive

    response_builder.set_code(ok_code)
    response_builder.set_message(ok_message)
    if connection:
        response_builder.set_connection(connection)
    return response_builder


def do_options(request, response_builder):
    response_builder = do_head(request, response_builder)
    response_builder.set_allow()
    return response_builder
