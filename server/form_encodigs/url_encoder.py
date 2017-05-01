
def parse(query):
    query_pars = query.split('&')
    data = {}
    for entry in query_pars:
        key, value = entry.split('=')
        data[key] = value
    return data
