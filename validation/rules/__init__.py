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
from .nullable import NullableRule
from .operationalfield import OperationalFieldRule
from .regex import RegexRule
from .required import RequiredRule

from .rule import Rule
from .ruleset import RuleSet

rules = {
    'alpha': AlphaRule,
    'alphadash': AlphaDashRule,
    'alphanum': AlphaNumRule,
    'between': BetweenRule,
    'betweenlen': BetweenLengthRule,
    'decimal': DecimalRule,
    'equals': EqualsRule,
    'equals_to': EqualsToRule,
    'file_format': FileFormatRule,
    'file_type': FileTypeRule,
    'hex': HexRule,
    'in': InRule,
    'len': LengthRule,
    'max': MaxRule,
    'max_size': MaxSizeRule,
    'maxlen': MaxLengthRule,
    'min': MinRule,
    'min_size': MinSizeRule,
    'minlen': MinLengthRule,
    'must_be_true': MustBeTrueRule,
    'nullable_if': NullableIfRule,
    'nullable': NullableRule,
    'operational_field_tmp_rule': OperationalFieldRule,
    'regex': RegexRule,
    'required': RequiredRule,
}
