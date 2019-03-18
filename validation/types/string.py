""" String """
from .type import Type
from ..constants import types


class StringType(Type):
    null_values = ['']

    @staticmethod
    def name() -> str:
        return types.STRING

    @classmethod
    def _validate_type(cls, value) -> bool:
        return isinstance(value, str)
