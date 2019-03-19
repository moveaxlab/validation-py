""" Equals """
from .rule import Rule
from ..constants import rules
from ..types import Type


class EqualsRule(Rule):
    required_params = 1
    supported_types = (Type,)

    @staticmethod
    def name() -> str:
        return rules.EQUALS

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the value is not equal to the target.
        return str(value) == self.target

    def _sanitize_params(self):
        self.target = self.params[0]
