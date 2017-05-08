from util.files import retrieve_file, retrieve_file_buffered
from template.template import Template
from storage.publications import PublicationsDAO

def get_html(path):
    if b"index.html" in path or path == b"/":
        html_data = retrieve_file(path)
        templ = Template(html_data)
        templ.compile()

        PublicationsDAO.create_publication("Author", "asdajkdsal", "text sa", "image/02fbcf46-1ac5-4db9-b6e6-cec46854e0c5.jpg")
        PublicationsDAO.create_publication("Author", "asdajkdsal", "text sa", "image/3d1b4132-9646-40ac-b77f-3f9bbb922272.jpg")
        PublicationsDAO.create_publication("Author", "asdajkdsal", "text sa", "image/02fbcf46-1ac5-4db9-b6e6-cec46854e0c5.jpg")
        PublicationsDAO.create_publication("Author", "asdajkdsal", "text sa", "image/02fbcf46-1ac5-4db9-b6e6-cec46854e0c5.jpg")
        data = PublicationsDAO.get_n_last_publications(4)

        html = templ.render({
            "posts": data,
            "edit_post": "/edit",
            "post_url": "/publication",
        })

        return html.encode()

    elif b'post' in path and b'create' not in path:
        id = path.split('/')[-1]
        publication = PublicationsDAO.get_publication(id)
        html_data = retrieve_file(path)
        templ = Template(html_data)
        templ.compile()
        templ.render({
            "post": publication
        })

    else:
        return retrieve_file_buffered(path)