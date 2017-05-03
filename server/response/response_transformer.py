from util.constants.const_main import *

def transform_response(response_obj):
    response = LF_BYTE
    response += SPACE_BYTE.join((response_obj.protocol, response_obj.code, response_obj.message)) + LF_BYTE
    for field in response_obj.headers:
        response += field + LF_BYTE
    response += LF_BYTE
    return response

