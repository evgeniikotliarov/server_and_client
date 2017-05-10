from util.files import retrieve_file
from util.path import get_filesystem_path
from util.constants.paths import *
from template.template import Template


_index_data = retrieve_file(get_filesystem_path(INDEX_PAGE))
index_template = Template(_index_data)
index_template.compile()
