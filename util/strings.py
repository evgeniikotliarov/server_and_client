def ensure_string(*byte_strings):


    def make_string(b_str):
        return b_str.decode() if isinstance(b_str, bytes) else str(b_str)

    for byte_str in byte_strings:
        yield make_string(byte_str)
