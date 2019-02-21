import string

from .rule import Rule


class AlphaNumRule(Rule):

    @staticmethod
    def name():
        return 'alphanum'

    def apply(self, data):
        for c in data:
            if c not in string.ascii_letters + string.digits:
                return False
        return True
