from paths import *
from template.template import Template
from util.files import retrieve_file

_base_data = retrieve_file(BASE_PAGE)


def render_base(data):
    base_template = Template(_base_data)
    base_template.compile()
    return base_template.render(data)


def insert_content(content):
    _base_data.replace("%content%", content)


print(_base_data)