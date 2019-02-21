class ValidatorSummary(object):

    def __init__(self, errors=None):
        if errors is None:
            errors = []
        self.errors = errors

    def empty(self):
        self.errors = []

    def merge(self, summary):
        self.add_errors(summary.errors)

    def add_error(self, error):
        self.errors.append(error)

    def add_errors(self, errors):
        for error in errors:
            self.add_error(error)

    def to_dict(self):
        return {
            'errors':
                [
                    {
                        "name": error.name,
                        "params": error.params,
                    }
                    for error in self.errors
                ]
        }