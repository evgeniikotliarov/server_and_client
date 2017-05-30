from server.requests.request_transformer import *

class RequestTransformerFactory:

    @staticmethod
    def create_transformer(raw_request):
        return RequestTransformer(raw_request)