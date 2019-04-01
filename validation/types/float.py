""" Float """
from .type import Type
from ..constants import types


class FloatType(Type):
    @staticmethod
    def name() -> str:
        return types.FLOAT

    @staticmethod
    def _validate_type(value) -> bool:
        return isinstance(value, (int, float))
