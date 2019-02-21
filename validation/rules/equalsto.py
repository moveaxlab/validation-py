from .rule import Rule


class EqualsToRule(Rule):

    @staticmethod
    def name():
        return 'equals_to'

    @classmethod
    def parse(cls, alias, spec, params_string):
        field1, field2 = params_string.split(',')
        return cls(alias=alias, field1=field1, field2=field2, spec=spec)

    def __init__(self, alias, field1, field2, spec):
        super().__init__(alias=alias, spec=spec)
        self.field1 = field1
        self.field2 = field2

    def apply(self, data):
        if self.field1 not in data or self.field2 not in data:
            return False
        return data[self.field1] == data[self.field2]

    def get_params(self):
        return [self.field1, self.field2]
