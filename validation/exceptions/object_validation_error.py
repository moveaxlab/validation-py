""" Object Validation Error """
from copy import deepcopy

from .validation_error import ValidationError
from ..constants import rules


class ObjectValidationError(ValidationError):
    def __init__(self, errors: list = None, schema_errors: dict = None):
        super().__init__(errors)
        self.schema_errors = schema_errors or {}

    def to_json(self) -> dict:
        return self._legacy_output({
            **super().to_json(),
            'schema_errors': {
                key: {
                    'errors': [err.to_json() for err in errors]
                } for key, errors in self.schema_errors.items()
            }
        })

    @staticmethod
    def _legacy_output(output) -> dict:
        legacy_output = deepcopy(output)
        required_error_obj = None
        for error in legacy_output['errors']:
            if error['name'] == rules.REQUIRED:
                required_error_obj = error
                for key in error['params']:
                    required_error = {'name': 'required', 'params': key, 'value': None}
                    legacy_output['schema_errors'][key] = {'errors': [required_error]}
        if required_error_obj:
            legacy_output['errors'].remove(required_error_obj)
        return legacy_output
