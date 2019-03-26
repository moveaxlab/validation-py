""" Nullable Error """
from .base_error import BaseError
from ..constants import rules


class NullableError(BaseError):
    """ Error that occurs on Nullable validation """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} should not be NULL'.format(self.value)

    @staticmethod
    def name() -> str:
        return "NullableError"

    def to_json(self) -> dict:
        return {'name': rules.NULLABLE,
                'value': self.value}
