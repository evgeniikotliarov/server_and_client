from storage.data_storages.memory import publications_storage

class Publications:
    def __init__(self, publication_storage):
        self.storage = publication_storage

    def create_publication(self, author, title, text, attachments=None,_id=None):
        return self.storage.create_publication(author, title, text, attachments, _id=_id)

    def delete_publication(self, _id):
        self.storage.delete_publication(_id)

    def replace_publication(self, _id, author, title, text):
        self.delete_publication(_id)
        self.create_publication(author, title, text, _id=_id)

    def get_publication(self, _id):
        return self.storage.get_publication(_id)

    def get_all_publications(self):
        return self.storage.get_all_publications

    def get_n_last_punlications(self, number=10):

        all_publications = self.storage.get_all_publications()
        for i, publ_id in enumerate(reversed(all_publications)):
            if i > number:
                break
            yield all_publications[publ_id]

PublicationsMemoryDAO = Publications(publications_storage)