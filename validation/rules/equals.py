from .rule import Rule


class EqualsRule(Rule):

    @staticmethod
    def name():
        return 'equals'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, value=params_string, spec=spec)

    def __init__(self, alias, value, spec):
        super().__init__(alias=alias, spec=spec)
        self.value = value

    def apply(self, data):
        return str(data) == self.value

    def get_params(self):
        return [self.value]
