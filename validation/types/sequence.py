""" Sequence """
from .type import Type
from ..constants import types


class SequenceType(Type):
    null_values = [[]]

    @staticmethod
    def name() -> str:
        return types.SEQUENCE

    @staticmethod
    def _validate_type(value) -> bool:
        return hasattr(value, '__iter__')
