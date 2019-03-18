""" Integer """
from .type import Type
from ..constants import types


class IntegerType(Type):
    @staticmethod
    def name() -> str:
        return types.INTEGER

    @staticmethod
    def _validate_type(value) -> bool:
        return isinstance(value, int)
