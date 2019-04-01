""" Equals To """
from .rule import Rule
from ..constants import rules
from ..types import ObjectType


class EqualsToRule(Rule):
    required_params = 2
    supported_types = (ObjectType,)

    @staticmethod
    def name() -> str:
        return rules.EQUALS_TO

    def _abides_by_the_rule(self, value: dict) -> bool:
        # Fail when the values of two keys are different.
        if self.key1 not in value or self.key2 not in value:
            return False
        return value[self.key1] == value[self.key2]

    def _sanitize_params(self):
        self.key1, self.key2 = self.params
