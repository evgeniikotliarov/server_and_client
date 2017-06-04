from template.const import *


class CodeBuilder:
    def __init__(self, indentation_level=0, indent_char=FOUR_SPACES):
        self._indentation_level = indentation_level
        self._code = []
        self._indent = indent_char
        self.add_result_buffer()

    def add_line(self, line):
        if not line: return
        self._code.extend([self._indent * self._indentation_level, line, NEWLINE])

    def extend_result(self, line):
        self.add_line("extend_result([%s])" % line)

    def __str__(self):
        return ''.join(str(c) for c in self._code)

    def indent(self):
        self._indentation_level += 1

    def dedent(self):
        self._indentation_level -= 1

    def execute(self, context):
        assert self._indentation_level == 0
        self.add_result_line()
        code = str(self)
        exec(code, {}, context)
        res = context['result']

        return res

    def add_result_buffer(self):
        self.add_line("_result = []")
        self.add_line("extend_result = _result.extend")
        self.add_line("append_result = _result.append")

        self.add_line('''
def _do_dots(value, *dots):
    for dot in dots:
        try:
            value = getattr(value, dot)
        except AttributeError:
            value = value[dot]
        if callable(value):
            value = value()

    return value
''')

    def add_result_line(self):
        self.add_line("result = ''.join(_result)")


