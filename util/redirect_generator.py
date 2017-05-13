from server.response.response_builder import *
from util.constants.response_codes import SEE_OTHER

def redirect_builder(location):
    response_builder = ResponseBuilder()
    code, message = SEE_OTHER
    response_builder.set_code(code)
    response_builder.set_message(message)
    response_builder.set_location(location)
    return response_builder
