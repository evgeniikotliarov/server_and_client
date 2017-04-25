class Publication:
    def __init__(self, user_id = None,  title = '', text = '', attachments = None):
        self.user_id = user_id
        self.title = title
        self.text = text
        self.attachments = attachments