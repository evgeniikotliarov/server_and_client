from server.entities.response import Response
from util.constants.headers import *


class ResponseBuilder:

    def __init__(self):
        self._response = Response()