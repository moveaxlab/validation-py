""" Decimal """
from decimal import Decimal

from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import StringType


class DecimalRule(Rule):
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.DECIMAL

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value is not a decimal string.
        try:
            Decimal(value)
            return True
        except Exception:
            return False

    def _sanitize_params(self):
        if self.params:
            raise SpecError(f'The DecimalRule takes no parameters')
