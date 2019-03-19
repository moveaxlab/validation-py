""" Object Validation Error """
from .validation_error import ValidationError


class ObjectValidationError(ValidationError):
    def __init__(self, errors: list = None, schema_errors: dict = None):
        super().__init__(errors)
        self.schema_errors = schema_errors or {}

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'schema_errors': {
                key: {
                    'errors': [err.to_json() for err in errors]
                } for key, errors in self.schema_errors.items()
            }
        }
