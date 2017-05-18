from util.constants.const_main import *
import os
from paths import LOGS_FOLDER


logs_file = os.path.join(LOGS_FOLDER, 'logs.txt')


def log(message):
    with open(logs_file, APPENT_BYTE) as file:
        file.write(LF_BYTE + message + LF_BYTE)


def log_request(request):
    log(b"Received request: " + SPACE_BYTE.join((request.method, request.target, request.protocol)))

def log_response(response):
    log(b"Sent response: " + SPACE_BYTE.join((response.method, response.target, response.protocol)))
