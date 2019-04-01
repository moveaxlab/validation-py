""" ValidationError """
from .error import Error


class ValidationError(Error):
    """ The validation error tree """
    def __init__(self, errors: list = None):
        self.errors = errors or []

    def get_errors(self) -> list:
        return self.errors

    def to_json(self) -> dict:
        return {
            'errors': [error.to_json() for error in self.errors]
        }
