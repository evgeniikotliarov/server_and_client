from paths import *
from template_engine.template import Template
from util.path import get_component_path
from util.files import retrieve_file

_index_data = retrieve_file(get_component_path(INDEX_PAGE))
index_template = Template(_index_data)
index_template.compile()

_publication_data = retrieve_file(get_component_path(PUBLICATION_PAGE))
publication_template = Template(_publication_data)
publication_template.compile()

_edit_page_data = retrieve_file(get_component_path(EDIT_PUBLICATION))
edit_page_template = Template(_edit_page_data)
edit_page_template.compile()

_profile_data = retrieve_file(get_component_path(PROFILE_PAGE))
profile_template = Template(_profile_data)
profile_template.compile()

