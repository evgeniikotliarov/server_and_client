from util.files import retrieve_file, retrieve_file_buffered
from template.template import Template
from storage.publications import PublicationsDAO

def get_html(path):
    if b"index.html" in path:
        html_data = retrieve_file(path)
        templ = Template(html_data)
        templ.compile()

        PublicationsDAO.create_publication("Me", "Заголовок 1", "Текст Первый")
        PublicationsDAO.create_publication("Me", "Заголовок 2", "Текст Второй")
        PublicationsDAO.create_publication("Me", "Заголовок 3", "Текст Третий")
        data = PublicationsDAO.get_n_last_publications(3)

        print(data[0].text)
        html = templ.render({
            "posts": data,
            "image": ("/image/Lorem-Ipsum-2.jpg"),
            "edit_post": "/edit",
            "post_url": "/publication/123",
        })

        return html.encode()
    else:
        return retrieve_file_buffered(path)