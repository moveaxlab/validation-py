""" Hex """
import string

from .rule import Rule
from ..constants import rules
from ..types import StringType


class HexRule(Rule):
    required_params = 0
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.HEX

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value is not hexadecimal
        return all(char in string.hexdigits for char in value)
