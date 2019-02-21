class ValidatorError(object):

    def __init__(self, name, params=None):
        if params is None:
            params = []
        self.name = name
        self.params = params