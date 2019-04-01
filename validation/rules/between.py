""" Between """
from .rule import Rule
from ..constants import rules
from ..types import FloatType, IntegerType


class BetweenRule(Rule):
    required_params = 2
    supported_types = (FloatType, IntegerType,)

    @staticmethod
    def name() -> str:
        return rules.BETWEEN

    def _abides_by_the_rule(self, value) -> bool:
        # Fails when the value goes beyond the [min, max] range.
        return self.min <= value <= self.max

    def _sanitize_params(self):
        self.min, self.max = self.params
        self.max = float(self.max)
        self.min = float(self.min)
