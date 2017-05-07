from util.files import retrieve_file
from template.template import Template

def get_html(path):
    if "index.html" in path:
        html_data = retrieve_file(path)
        templ = Template(html_data)
        templ.compile()
        templ.render({

        })