from paths import *
from template.template import Template
from util.files import retrieve_file
from util.path import get_filesystem_path

_index_data = retrieve_file(get_filesystem_path(INDEX_PAGE))
index_template = Template(_index_data)
index_template.compile()

_publication_data = retrieve_file(get_filesystem_path(PUBLICATION_PAGE))
publication_template = Template(_publication_data)
publication_template.compile()

_profile_data = retrieve_file(get_filesystem_path(PROFILE_PAGE))
profile_template = Template(_profile_data)
profile_template.compile()