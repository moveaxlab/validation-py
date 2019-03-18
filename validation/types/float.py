""" Float """
from .type import Type
from ..constants import types


class FloatType(Type):
    @staticmethod
    def name() -> str:
        return types.FLOAT

    @classmethod
    def _validate_type(cls, value) -> bool:
        return isinstance(value, (int, float))
