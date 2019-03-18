""" Array Validation Error """
from .validation_error import ValidationError


class ArrayValidationError(ValidationError):
    def __init__(self, elements_errors=None, errors=None):
        super().__init__(errors)
        self.elements_errors = elements_errors or []

    def to_json(self) -> dict:
        return {
            **super().to_json(),
            'elements_errors': [element_error.to_json() for element_error in self.elements_errors]
        }
