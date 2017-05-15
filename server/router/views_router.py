from util.files import retrieve_file, retrieve_file_buffered
from template.template import Template
from storage.publications import PublicationsMemoryDAO
from util.constants.paths import *
from template.compiled_templates import index_template

def get_html(path):
    if isHtml(path):
        if isIndex(path):
            return build_index()

    elif 'post' in path and 'create' not in path: #TODO можно переделать это
        _id = path.split('/')[-1]
        publication = PublicationsMemoryDAO.get_publication(_id)
        html_data = retrieve_file(path)
        template = Template(html_data)
        template.compile()
        template.render({
            "post": publication
        })

    else:
        return retrieve_file_buffered(path)


def build_index():
    data = PublicationsMemoryDAO.get_all_publication()
    html = index_template.render({
        "post": data,
        "edit_post_utl": "/edit",
        "post_url": "/publication",
    })

    return html.encode()


def isHtml(path):
    return path.endswith('.html')

def isIndex(path):
    return path.endswith(INDEX_PAGE)
