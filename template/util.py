def to_string(text):
    return "str(%s)" %text

def throw_error(message, who_threw):
    raise TemlateError(message, who_threw)

def is_expression(token):
    return token.startswith('{{')

def is_control(token):
    return token.startswith('{%')

class TemplateError(Exception):
    pass

