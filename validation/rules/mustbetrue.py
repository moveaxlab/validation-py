from .rule import Rule


class MustBeTrueRule(Rule):

    @staticmethod
    def name():
        return 'must_be_true'

    def apply(self, data):
        return data is True
