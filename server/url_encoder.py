query = 'name=vasya&password=123456&age=120'
def string_parser(query):
    query_pars = query.split('&')
    data = {}
    for entry in query_pars:
        key, value = entry.split('=')
        data[key] = value
    return data
