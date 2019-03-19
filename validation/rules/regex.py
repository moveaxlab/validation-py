""" Regex """
import re

from .rule import Rule
from ..constants import rules
from ..types import StringType


class RegexRule(Rule):
    required_params = 1
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.REGEX

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the regex does not match
        return self.regex.search(value) is not None

    def _sanitize_params(self):
        self.regex = re.compile(self.params[0])
