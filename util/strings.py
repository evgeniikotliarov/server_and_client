def bytes_to_strings(*byte_strings):
    for byte_str in byte_strings:
        if isinstance(byte_str, bytes):
            yield byte_str.decode()
        else:
            yield str(byte_str)
