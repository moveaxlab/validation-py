from .alpha import AlphaRule
from .alphadash import AlphaDashRule
from .alphanum import AlphaNumRule
from .between import BetweenRule
from .betweenlength import BetweenLengthRule
from .decimal import DecimalRule
from .equals import EqualsRule
from .equalsto import EqualsToRule
from .fileformat import FileFormatRule
from .filetype import FileTypeRule
from .hex import HexRule
from .isin import InRule
from .len import LengthRule
from .max import MaxRule
from .maxlength import MaxLengthRule
from .maxsize import MaxSizeRule
from .min import MinRule
from .minlength import MinLengthRule
from .minsize import MinSizeRule
from .mustbetrue import MustBeTrueRule
from .nullableif import NullableIfRule
from .phonetype import PhoneTypeRule
from .regex import RegexRule
from .required import RequiredRule
from .rule import Rule
from .strict import StrictRule
from ..constants.rules import *

rules = {
    ALPHA: AlphaRule,
    ALPHADASH: AlphaDashRule,
    ALPHANUM: AlphaNumRule,
    BETWEEN: BetweenRule,
    BETWEENLEN: BetweenLengthRule,
    DECIMAL: DecimalRule,
    EQUALS: EqualsRule,
    EQUALS_TO: EqualsToRule,
    FILE_FORMAT: FileFormatRule,
    FILE_TYPE: FileTypeRule,
    HEX: HexRule,
    IN: InRule,
    LEN: LengthRule,
    MAX: MaxRule,
    MAX_SIZE: MaxSizeRule,
    MAXLEN: MaxLengthRule,
    MIN: MinRule,
    MIN_SIZE: MinSizeRule,
    MINLEN: MinLengthRule,
    MUST_BE_TRUE: MustBeTrueRule,
    NULLABLE_IF: NullableIfRule,
    PHONE_TYPE: PhoneTypeRule,
    REGEX: RegexRule,
    REQUIRED: RequiredRule,
    STRICT: StrictRule,
}
