from .array import ArrayType
from .base58 import Base58Type
from .base64 import Base64Type
from .base64file import Base64EncodedFileType
from .boolean import BooleanType
from .composite import CompositeType
from .email import EmailType
from .float import FloatType
from .integer import IntegerType
from .iso8601date import ISO8601DateType
from .object import ObjectType
from .phone import PhoneType
from .sequence import SequenceType
from .string import StringType
from .type import Type
from .url import URLType
from .uuid import UUIDType
from ..constants.types import *

types = {
    ARRAY: ArrayType,
    BASE58: Base58Type,
    BASE64: Base64Type,
    BASE64_ENCODED_FILE: Base64EncodedFileType,
    BOOLEAN: BooleanType,
    COMPOSITE: CompositeType,
    EMAIL: EmailType,
    FLOAT: FloatType,
    INTEGER: IntegerType,
    ISO_8601_DATE: ISO8601DateType,
    OBJECT: ObjectType,
    PHONE: PhoneType,
    SEQUENCE: SequenceType,
    STRING: StringType,
    URL: URLType,
    UUID: UUIDType,
}
