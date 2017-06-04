from paths import *
from template.template_engine import Template
from util.files import retrieve_file

_base_data = ''


def render_base(data):

    base_template = Template(_base_data)
    base_template.compile()
    return base_template.render(data).encode()


def insert_content(content):
    global _base_data
    _base_data = retrieve_file(BASE_PAGE)
    _base_data = _base_data.replace("%content%", content)
    return _base_data

