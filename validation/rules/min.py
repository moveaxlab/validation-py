from .rule import Rule


class MinRule(Rule):

    @staticmethod
    def name():
        return 'min'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, minimum=int(params_string), spec=spec)

    def __init__(self, alias, minimum, spec):
        super().__init__(alias=alias, spec=spec)
        self.min = minimum

    def apply(self, data):
        return data >= self.min

    def get_params(self):
        return [self.min]
