""" Array Validation Error """
from .validation_error import ValidationError


class ArrayValidationError(ValidationError):
    def __init__(self, elements_errors: list = None, errors: list = None):
        super().__init__(errors)
        self.elements_errors = elements_errors or []

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'elements_errors': [error.to_json() for error in self.elements_errors]
        }
