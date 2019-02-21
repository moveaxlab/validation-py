from .rule import Rule


class RequiredRule(Rule):

    @staticmethod
    def name():
        return 'required'

    def apply(self, data):
        return True
