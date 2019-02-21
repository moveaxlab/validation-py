from .validator_summary import ValidatorSummary


class ObjectValidatorSummary(ValidatorSummary):

    def __init__(self, errors=None, schema_errors=None):
        super().__init__(errors)
        if schema_errors == None:
            schema_errors = {}
        self.schema_errors = schema_errors

    def _check_and_add_key(self, key, summary_class):
        if key not in self.schema_errors:
            self.schema_errors[key] = ValidatorSummary()
        if not isinstance(self.schema_errors[key], summary_class):
            new_summary = summary_class()
            new_summary.merge(self.schema_errors[key])
            self.schema_errors[key] = new_summary


    def empty(self):
        super(ObjectValidatorSummary, self).empty()
        self.schema_errors = {}

    def merge(self, summary):
        super(ObjectValidatorSummary, self).merge(summary)
        if isinstance(summary, ObjectValidatorSummary):
            for key, schema_error in summary.schema_errors.items():
                self.add_schema_errors(key, schema_error)

    def add_schema_error(self, key, error):
        self._check_and_add_key(key, ValidatorSummary)
        self.schema_errors[key].add_error(error)

    def add_schema_errors(self, key, errors):
        self._check_and_add_key(key, errors.__class__)
        self.schema_errors[key].merge(errors)

    def to_dict(self):
        result = super(ObjectValidatorSummary, self).to_dict()
        result['schema_errors'] = {
            key: error.to_dict()
            for key, error in self.schema_errors.items()
        }
        return result
