from util.id_generator import generate_id

class Publication:
    def __init__(self, author = None, title = "", text = "", attachments = None):
        self.author = author
        self.title = title
        self.text = text
        self.attachments = attachments
        self._id = generate_id()

    def set_id(self):
        return self._id

    def set_text(self):
        pass

    def set_title(self):
        pass

    def set_attacment(self):
        pass
