from .rule import Rule


class BetweenLengthRule(Rule):

    @staticmethod
    def name():
        return 'betweenlen'

    @classmethod
    def parse(cls, alias, spec, params_string):
        minlen, maxlen = params_string.split(',')
        return cls(alias=alias, minlen=int(minlen), maxlen=int(maxlen), spec=spec)

    def __init__(self, alias, minlen, maxlen, spec):
        super().__init__(alias=alias, spec=spec)
        self.minlen = minlen
        self.maxlen = maxlen

    def apply(self, data):
        return self.minlen <= len(data) <= self.maxlen

    def get_params(self):
        return [self.minlen, self.maxlen]
