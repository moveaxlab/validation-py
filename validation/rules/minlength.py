""" Min Length """
from .rule import Rule
from ..constants import rules
from ..types import SequenceType


class MinLengthRule(Rule):
    supported_types = (SequenceType,)

    @staticmethod
    def name() -> str:
        return rules.MINLEN

    def _abides_by_the_rule(self, value) -> bool:
        # Fail if the value's length is lower than min_length
        return len(value) >= self.min_length

    def _sanitize_params(self):
        self.min_length = int(self.params[0])
