""" Alpha Num """
from .rule import Rule
from ..constants import rules
from ..types import StringType


class AlphaNumRule(Rule):
    required_params = 0
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.ALPHANUM

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value has non alphanumeric characters.
        return value.isalnum()
