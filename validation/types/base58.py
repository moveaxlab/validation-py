""" Base58 """
import re

from .string import StringType
from ..constants import types

# Constants
BASE58_RE = re.compile(r'^[1-9A-HJ-NP-Za-km-z]+$')


class Base58Type(StringType):
    @staticmethod
    def name() -> str:
        return types.BASE58

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        return BASE58_RE.match(value) is not None
