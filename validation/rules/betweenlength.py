""" Between Length """
from .rule import Rule
from ..constants import rules
from ..types import SequenceType, StringType


class BetweenLengthRule(Rule):
    required_params = 2
    supported_types = (SequenceType, StringType,)

    @staticmethod
    def name() -> str:
        return rules.BETWEENLEN

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the length of the value goes beyond the [min, max] range.
        return self.min <= len(value) <= self.max

    def _sanitize_params(self):
        self.min, self.max = self.params
        self.max = int(self.max)
        self.min = int(self.min)
