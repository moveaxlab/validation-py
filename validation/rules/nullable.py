from .rule import Rule


class NullableRule(Rule):

    @staticmethod
    def name():
        return 'nullable'

    def apply(self, data):
        return True
