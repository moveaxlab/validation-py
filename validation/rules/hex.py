""" Hex """
import string

from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import StringType


class HexRule(Rule):
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.HEX

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value is not hexadecimal
        return all(char in string.hexdigits for char in value)

    def _sanitize_params(self):
        if self.params:
            raise SpecError(f'The HexRule takes no parameters')
