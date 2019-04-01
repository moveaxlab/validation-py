""" Alpha """
from .rule import Rule
from ..constants import rules
from ..types import StringType


class AlphaRule(Rule):
    required_params = 0
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.ALPHA

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value has non alphabetic characters.
        return value.isalpha()
