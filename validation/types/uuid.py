""" UUID """
from uuid import UUID

from . import StringType
from ..constants import types


class UUIDType(StringType):
    @staticmethod
    def name() -> str:
        return types.UUID

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        try:
            created = UUID(value, version=4)
        except ValueError:
            return False
        return value == str(created)
