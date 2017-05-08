def ensure_string(*byte_strings):

    def make_string(byte_str):
        if isinstance(byte_str, bytes):
            yield byte_str.decode()
        else:
            yield str(byte_str)

    if len(byte_strings) == 1:
        return make_string(byte_strings[0])

    for byte_str in byte_strings:
        yield make_string(byte_str)
