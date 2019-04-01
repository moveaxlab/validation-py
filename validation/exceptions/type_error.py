""" TypeError """
from .base_error import BaseError


class TypeError(BaseError):
    """ Error that occurs on Type validation """
    def __init__(self, type, value):
        self.type_name = type.name()
        self.value = value

    def __str__(self) -> str:
        return '{} is not type {}'.format(self.value, self.type_name)

    @staticmethod
    def name() -> str:
        return "TypeError"

    def to_json(self) -> dict:
        return {
            'name': self.type_name,
            'value': self.value
        }
