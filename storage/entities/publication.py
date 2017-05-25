from util.id_generator import generate_id


class Publication:
    def __init__(self, author=None, title="", text="", attachments=None):
        self.author = author
        self.title = title
        self.text = text
        self.attachments = attachments
        self._id = generate_id()

    def get_id(self):
        return self._id

    def get_first_attachments(self):
        return self.attachments[0] if self.attachments else None