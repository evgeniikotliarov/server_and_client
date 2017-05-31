
class Route:
    def __init__(self, methods, paths, handler):
        self.methods = methods
        self.paths = paths
        self.handler = handler

    def get_handler(self):
        return self.handler

    def has_method(self, method):
        if type(self.methods) == list or type(self.methods) == tuple:
            return method in self.methods
        else:
            return method == self.methods

    def has_path(self, path):
        if type(self.paths) == list or type(self.paths) == tuple:
            return path in self.paths
        else:
            return path == self.paths
