""" Base64 """
import re

from .string import StringType
from ..constants import types

# Constants
BASE64_RE = re.compile(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')


class Base64Type(StringType):
    @staticmethod
    def name() -> str:
        return types.BASE64

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        return BASE64_RE.match(value) is not None
