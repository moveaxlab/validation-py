""" Object Validation Error """
from .validation_error import ValidationError


class ObjectValidationError(ValidationError):
    def __init__(self, errors=None, schema_errors=None):
        super().__init__(errors)
        self.schema_errors = schema_errors or []

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'schema_errors': [key_error.to_json() for key_error in self.schema_errors]
        }
