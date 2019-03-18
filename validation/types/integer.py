""" Integer """
from .type import Type
from ..constants import types


class IntegerType(Type):
    @staticmethod
    def name() -> str:
        return types.INTEGER

    @classmethod
    def _validate_type(cls, value) -> bool:
        return isinstance(value, int)
