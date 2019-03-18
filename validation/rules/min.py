""" Min """
from .rule import Rule
from ..constants import rules
from ..types import FloatType, IntegerType


class MinRule(Rule):
    supported_types = (FloatType, IntegerType,)

    @staticmethod
    def name() -> str:
        return rules.MIN

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the value is lower than the target.
        return float(value) >= self.target

    def _sanitize_params(self):
        self.target = float(self.params[0])
