""" Boolean """
from .type import Type
from ..constants import types


class BooleanType(Type):
    @staticmethod
    def name() -> str:
        return types.BOOLEAN

    @classmethod
    def _validate_type(cls, value) -> bool:
        return isinstance(value, bool)
