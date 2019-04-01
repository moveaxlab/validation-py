""" Object """
from . import CompositeType
from ..constants import types


class ObjectType(CompositeType):
    @staticmethod
    def name() -> str:
        return types.OBJECT

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        return isinstance(value, dict)
