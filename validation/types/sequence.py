""" Sequence """
from .type import Type
from ..constants import types


class SequenceType(Type):
    null_values = [[]]

    @staticmethod
    def name() -> str:
        return types.SEQUENCE

    @classmethod
    def _validate_type(cls, value) -> bool:
        return hasattr(value, '__iter__')
