from util.constants.const_main import *

def transform_response(response_obj):
    response = LF_BYTE
    proto = response_obj.rotocol
    code = response_obj.code
    msg = response_obj.message
    response += SPACE_BYTE.join((proto, code, msg) + LF_BYTE
    for field in response_obj.headers:
        response += field + LF_BYTE
    response += LF_BYTE
    return response

