from util.redirect import do_redirect
from paths import ERROR_PAGE


def do_error(error, request, response_builder):
    return do_redirect(ERROR_PAGE, response_builder)