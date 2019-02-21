from .rule import Rule


class LengthRule(Rule):

    @staticmethod
    def name():
        return 'len'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, length=int(params_string), spec=spec)

    def __init__(self, alias, length, spec):
        super().__init__(alias=alias, spec=spec)
        self.len = length

    def apply(self, data):
        return len(data) == self.len

    def get_params(self):
        return [self.len]
