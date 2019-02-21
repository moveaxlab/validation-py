from .rule import Rule


class MaxRule(Rule):

    @staticmethod
    def name():
        return 'max'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, maximum=int(params_string), spec=spec)

    def __init__(self, alias, maximum, spec):
        super().__init__(alias=alias, spec=spec)
        self.max = maximum

    def apply(self, data):
        return data <= self.max

    def get_params(self):
        return [self.max]
