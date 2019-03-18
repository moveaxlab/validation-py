""" Alpha """
import string

from .rule import Rule
from ..constants import rules


class AlphaRule(Rule):
    def apply(self, value) -> bool:
        for char in value:
            if char not in string.ascii_letters:
                return False
        return True

    @staticmethod
    def name() -> str:
        return rules.ALPHA
