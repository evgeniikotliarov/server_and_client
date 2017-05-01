from util.constants.const_main import *
from server.actions.static_actions import *

routes = {
    GET: do_get,
    HEAD: do_head,
    OPTIONS: do_options,

    #REGISTER: #TODO implement action methods
}