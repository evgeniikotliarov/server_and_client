import time
from util.constants.const_main import *

def get_raw_request(connection, timeout=1):
    connection.setblocking(0)
    data = []
    start = time.time()
    time_is_up = lambda: time() - start > timeout

    while True:
        if time_is_up(): break
        try:
            data = connection.recv(REQUEST_RECV_SIZE)
            if data:
                data.append(data)
                start = time.time()
            else:
                time.sleep(0.1)
        except connection.error:
            pass # TODO error handling here

    return b''.join(data)