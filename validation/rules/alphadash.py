""" Alpha Dash """
import string

from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import StringType


class AlphaDashRule(Rule):
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.ALPHADASH

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value has non alphabetic characters or has special chars other than "-" and "_".
        return all(char in string.ascii_letters + '-_' for char in value)

    def _sanitize_params(self):
        if self.params:
            raise SpecError(f'The AlphaDashRule takes no parameters')
