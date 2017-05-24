from server.actions.get_pages import *

def head_index(request, response_builder):
    return get_index(request, response_builder)


def head_publication(request, response_builder):
    return get_publication(request, response_builder)


def head_profile(request, response_builder):
    return get_profile(request, response_builder)


def head_static(request, response_builder):
    return get_static(request, response_builder)

