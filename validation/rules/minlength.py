""" Min Length """
from .rule import Rule
from ..constants import rules
from ..types import SequenceType, StringType


class MinLengthRule(Rule):
    required_params = 1
    supported_types = (SequenceType, StringType,)

    @staticmethod
    def name() -> str:
        return rules.MINLEN

    def _abides_by_the_rule(self, value) -> bool:
        # Fail if the value's length is lower than min_length.
        return len(value) >= self.min_length

    def _sanitize_params(self):
        self.min_length = int(self.params[0])
