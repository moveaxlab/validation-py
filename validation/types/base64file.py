""" Base64 File """
import re

from .string import StringType
from ..constants import types

# Constants
BASE64_FILE_RE = re.compile(
    r'^'  # beginning of string
    r'data:(?P<type>[a-z]+)/(?P<format>[a-z]+);base64,'  # header
    r'(?:[A-Za-z0-9+/]{4})*'
    r'(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    r'$')  # end of string


class Base64EncodedFileType(StringType):
    @staticmethod
    def name() -> str:
        return types.BASE64_ENCODED_FILE

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        return BASE64_FILE_RE.match(value) is not None
