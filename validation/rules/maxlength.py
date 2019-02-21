from .rule import Rule


class MaxLengthRule(Rule):

    @staticmethod
    def name():
        return 'maxlen'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, maxlen=int(params_string), spec=spec)

    def __init__(self, alias, maxlen, spec):
        super().__init__(alias=alias, spec=spec)
        self.maxlen = maxlen

    def apply(self, data):
        return len(data) <= self.maxlen

    def get_params(self):
        return [self.maxlen]
