""" String """
from .type import Type
from ..constants import types


class StringType(Type):
    null_values = ['']

    @staticmethod
    def name() -> str:
        return types.STRING

    @staticmethod
    def _validate_type(value) -> bool:
        return isinstance(value, str)
