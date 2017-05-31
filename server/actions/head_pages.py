from server.actions.get_pages import *


def head_index(request, response_builder):
    rb = get_index(request, response_builder).set_body(None)
    return rb


def head_publication(request, response_builder):
    rb = get_index(request, response_builder).set_body(None)
    return rb


def head_profile(request, response_builder):
    rb = get_profile(request, response_builder).set_body(None)
    return rb


def head_static(request, response_builder):
    rb = get_static(request, response_builder).set_body(None)
    return rb


def head_edit_post(request, response_builder):
    rb = get_edit_post(request, response_builder).set_body(None)
    return rb
