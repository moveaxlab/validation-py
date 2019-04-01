""" Must Be True """
from .rule import Rule
from ..constants import rules
from ..types import BooleanType


class MustBeTrueRule(Rule):
    required_params = 0
    supported_types = (BooleanType,)

    @staticmethod
    def name() -> str:
        return rules.MUST_BE_TRUE

    def _abides_by_the_rule(self, value) -> bool:
        # Fail if value is Falsy
        return value is True
