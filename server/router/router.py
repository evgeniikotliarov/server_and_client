from util.constants.const_main import *
import server.router.action_router as action_router
import server.router.static_router as static_router

def route(request):
    method = request.method
    if is_action(method):
        action_router.route(request)
    elif is_static(method):
        static_router.route(request)
    #else TODO rhrow error - wtf he wants me to do

def is_action(method):
    return method in METHODS_ALLOWING_ACTION

def is_static(method):
    return method not in METHODS_ALLOWING_ACTION