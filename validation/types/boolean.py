""" Boolean """
from .type import Type
from ..constants import types


class BooleanType(Type):
    @staticmethod
    def name() -> str:
        return types.BOOLEAN

    @staticmethod
    def _validate_type(value) -> bool:
        return isinstance(value, bool)
