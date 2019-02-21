from .rule import Rule


class MinLengthRule(Rule):

    @staticmethod
    def name():
        return 'minlen'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, minlen=int(params_string), spec=spec)

    def __init__(self, alias, minlen, spec):
        super().__init__(alias=alias, spec=spec)
        self.minlen = minlen

    def apply(self, data):
        return len(data) >= self.minlen

    def get_params(self):
        return [self.minlen]
