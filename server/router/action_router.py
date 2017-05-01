from server.form_encodings.multipart import *


def route(request):
    path = request.target

    if is_multipart(request):
        multipart_fields = wrap_multipart(request)
        #TODO implement the usage of multipart fields