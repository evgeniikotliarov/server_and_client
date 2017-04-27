import uuid
class Publication:
    def __init__(self, user_id = None, title = "", text = "", attachments = None):
        self.user_id = user_id
        self.title = title
        self.text = text
        self.attachments = attachments
        self.unique_id = str(uuid.uuid4())

    def get_id(self):
        return self.unique_id

    def set_id(self):
        pass

    def set_text(self):
        pass

    def set_title(self):
        pass

    def set_attacment(self):
        pass