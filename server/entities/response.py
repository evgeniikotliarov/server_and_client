from datetime import datetime, tzinfo, timedelta
from util.constants.headers import *

class Response:
    def __init__(self):
        self.code = None
        self.message = None
        self.protocol = None
        self.headers = []
        self.body = None

