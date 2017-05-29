from util.redirect import do_redirect
from paths import NOT_FOUND_PAGE


def do_not_found_error(error, request, response_builder):
    return do_redirect(NOT_FOUND_PAGE, response_builder)