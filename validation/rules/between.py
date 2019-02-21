from .rule import Rule


class BetweenRule(Rule):

    @staticmethod
    def name():
        return 'between'

    @classmethod
    def parse(cls, alias, spec, params_string):
        minimum, maximum = params_string.split(',')
        return cls(alias=alias, minimum=int(minimum), maximum=int(maximum), spec=spec)

    def __init__(self, alias, minimum, maximum, spec):
        super().__init__(alias=alias, spec=spec)
        self.min = minimum
        self.max = maximum

    def apply(self, data):
        return self.min <= data <= self.max

    def get_params(self):
        return [self.min, self.max]
