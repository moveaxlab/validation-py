from .rule import Rule


class InRule(Rule):

    @staticmethod
    def name():
        return 'in'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, collection=params_string.split(','), spec=spec)

    def __init__(self, alias, collection, spec):
        super().__init__(alias, spec)
        self.collection = collection

    def apply(self, data):
        return str(data) in self.collection

    def get_params(self):
        return [",".join(self.collection)]
