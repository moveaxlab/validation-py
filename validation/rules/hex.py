import string

from .rule import Rule


class HexRule(Rule):

    @staticmethod
    def name():
        return 'hex'

    def apply(self, data):
        for c in data:
            if c not in string.hexdigits:
                return False
        return True
