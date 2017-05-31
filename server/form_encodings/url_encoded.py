from util.strings import ensure_string


def parse_url_encoded(query):
    query = next(ensure_string(query))
    query_pars = query.split('&')
    data = {}
    for entry in query_pars:
        key, value = entry.split("=")
        data[key] = value
    return data