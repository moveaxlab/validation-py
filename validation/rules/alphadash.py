import string

from .rule import Rule


class AlphaDashRule(Rule):

    @staticmethod
    def name():
        return 'alphadash'

    def apply(self, data):
        for c in data:
            if c not in string.ascii_letters + string.digits + '-_':
                return False
        return True
