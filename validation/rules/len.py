""" Length """
from .rule import Rule
from ..constants import rules
from ..types import SequenceType, StringType


class LengthRule(Rule):
    required_params = 1
    supported_types = (SequenceType, StringType,)

    @staticmethod
    def name() -> str:
        return rules.LEN

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the length of the value is different from the target.
        return len(value) == self.target

    def _sanitize_params(self):
        self.target = int(self.params[0])
