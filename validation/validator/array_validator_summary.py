from .validator_summary import ValidatorSummary


class ArrayValidatorSummary(ValidatorSummary):

    def __init__(self, errors=None, elements_errors=None):
        super().__init__(errors)
        if elements_errors == None:
            elements_errors = []
        self.elements_errors = elements_errors

    def empty(self):
        super(ArrayValidatorSummary, self).empty()
        self.elements_errors = []

    def merge(self, summary):
        super(ArrayValidatorSummary, self).merge(summary)
        if isinstance(summary, ArrayValidatorSummary):
            self.add_elements_errors(summary.elements_errors)

    def add_elements_errors(self, errors):
        self.elements_errors += errors

    def to_dict(self):
        result = super(ArrayValidatorSummary, self).to_dict()
        result['elements_errors'] = [error.to_dict() for error in self.elements_errors]
        return result