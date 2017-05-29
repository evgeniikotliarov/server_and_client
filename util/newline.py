from util.constants.const_main import *


def get_newline_char(text):
    is_in_text = lambda char: text.find(char) >= 0

    if type(text) == bytes:
        return CRLF_BYTE if is_in_text(CRLF_BYTE) else LF_BYTE
    else:
        return CRLF if is_in_text(CRLF) else LF