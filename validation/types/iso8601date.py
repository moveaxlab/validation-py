""" ISO8601 formatted date """
from dateutil.parser import isoparse

from .string import StringType
from ..constants import types


class ISO8601DateType(StringType):
    @staticmethod
    def name() -> str:
        return types.ISO_8601_DATE

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        try:
            isoparse(value)
            return True
        except ValueError:
            return False
