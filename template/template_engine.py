from template.code_builder import *
import re


class Template:
    def __init__(self, text):
        self._text = text
        self.tokens = tokenize(text)
        self.builder = CodeBuilder()
        self._buffer = []

    def compile(self):
        for token in self.tokens:
            token = token.strip(SPACING_CHARS)
            if not token: continue
            if is_expression(token):
                result = self.transform_expr(token)
                self._buffer.append(to_string(result))
            elif is_control(token):
                self._flush_buffer()
                self.do_control(token)
            else:
                self._buffer.append(repr(token))
        self._flush_buffer()

    def render(self, context):
        return self.builder.execute(context)

    def transform_expr(self, token):
        expr = token[2:-2].strip()
        return self._do_expr(expr)

    def do_control(self, token):
        tokens = token[2:-2].strip().split()
        if tokens[0] == IF:
            self.ensure_tokens_length(tokens, 2)
            condition = self._do_expr(tokens[1])
            self.builder.add_line("if %s:" % condition)
            self.builder.indent()

        if tokens[0] == ELSE:
            self.ensure_tokens_length(tokens, 1)
            self.builder.add_line("else:")
            self.builder.indent()

        elif tokens[0] == FOR:
            self.ensure_tokens_length(tokens, 4)
            variable, loop_target = tokens[1], tokens[3]
            self.builder.add_line("for %s in %s:" % (variable, loop_target))
            self.builder.indent()

        elif tokens[0].startswith('end'):
            # TODO validation
            self.builder.dedent()

    def ensure_tokens_length(self, tokens, num):
        if len(tokens) != num:
            expr = " ".join(tokens)
            raise TemplateError("Error at: %s" % expr)

    def _do_expr(self, expr):
        if PIPELINE in expr:
            result = self.handle_pipeline(expr)
        elif DOT in expr:
            tokens = expr.split(DOT)
            target = self._do_expr(tokens[0])
            args = ", ".join(repr(arg) for arg in tokens[1:])
            result = "_do_dots(%s, %s)" % (target, args)
        else:
            result = expr
        return str(result)

    def handle_pipeline(self, expr):
        tokens = expr.split(PIPELINE)
        var = tokens[0]
        for func in tokens[1:]:
            return "%s(%s)" % (func, var)

    def _flush_buffer(self):
        if not self._buffer: return
        buf = ', '.join(self._buffer)
        self.builder.add_line(self.builder.extend_result(buf))
        self._buffer = []



def tokenize(text):
    from util.regexes import get_template_tokenizer_regex
    reg = get_template_tokenizer_regex()
    tokens = re.split(reg, text)
    return tokens

def to_string(text):
    return "str(%s)" % text


def throw_error(message, who_threw):
    raise TemplateError(message, who_threw)


def is_expression(token):
    return token.startswith('{{')


def is_control(token):
    return token.startswith('{%')


class TemplateError(Exception):
    pass

