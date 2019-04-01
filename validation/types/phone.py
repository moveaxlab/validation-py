""" Phone """
import re

import phonenumbers

from .string import StringType
from ..constants import types

# Constants
PHONE_RE = re.compile(r'^\s*\+(\s*\(?\d\)?-?)*\s*$')


class PhoneType(StringType):
    @staticmethod
    def name() -> str:
        return types.PHONE

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        if PHONE_RE.match(value) is None:
            return False
        try:
            number = phonenumbers.parse(value, None)
        except phonenumbers.NumberParseException:
            return False
        return phonenumbers.is_valid_number(number)
