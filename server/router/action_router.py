from server.multipart import *
from server.actions.registration import *
from server.actions.publish import *

def get_action(request):
    path = request.target

    if is_multipart(request):
        multipart_fields = wrap_multipart(request)
        #TODO implement the usage of multipart fields
