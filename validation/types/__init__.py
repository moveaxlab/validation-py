from .array import Array
from .base64 import Base64
from .base64file import Base64EncodedFile
from .base58 import Base58
from .boolean import Boolean
from .email import Email
from .float import Float
from .integer import Integer
from .iso8601date import ISO_8601_Date
from .object import Object
from .phone import Phone
from .sequence import Sequence
from .string import String
from .url import URL
from .uuid import UUID

from .type import Type

types = {
    'array': Array,
    'base64': Base64,
    'base64_encoded_file': Base64EncodedFile,
    'base58': Base58,
    'boolean': Boolean,
    'email': Email,
    'float': Float,
    'integer': Integer,
    'ISO_8601_date': ISO_8601_Date,
    'object': Object,
    'phone': Phone,
    'sequence': Sequence,
    'string': String,
    'url': URL,
    'uuid': UUID,
}
