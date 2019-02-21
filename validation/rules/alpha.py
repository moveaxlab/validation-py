import string

from .rule import Rule


class AlphaRule(Rule):

    @staticmethod
    def name():
        return 'alpha'

    def apply(self, data):
        for c in data:
            if c not in string.ascii_letters:
                return False
        return True
