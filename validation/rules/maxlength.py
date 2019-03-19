""" Max Length """
from .rule import Rule
from ..constants import rules
from ..types import SequenceType, StringType


class MaxLengthRule(Rule):
    required_params = 1
    supported_types = (SequenceType, StringType,)

    @staticmethod
    def name() -> str:
        return rules.MAXLEN

    def _abides_by_the_rule(self, value) -> bool:
        # Fail if the value's length is greater than max_length.
        return len(value) <= self.max_length

    def _sanitize_params(self):
        self.max_length = int(self.params[0])
