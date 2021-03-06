import time

from util.constants.const_main import *


def get_raw_request(connection, timeout=0.3):
    connection.setblocking(0)
    all_data = []
    start = time.time()
    def time_is_up(): return time.time() - start > timeout

    while True:
        if time_is_up(): break
        try:
            data = connection.recv(REQUEST_RECV_SIZE)
            if data:
                all_data.append(data)
                start = time.time()
            else:
                time.sleep(0.1)
        except socket.error:
            pass

    return EMPTY_BYTE_STR.join(all_data)