from .rule import Rule


class NullableIfRule(Rule):

    @staticmethod
    def name():
        return 'nullable_if'

    @classmethod
    def parse(cls, alias, spec, params_string):
        check, field = params_string.split(',')
        return cls(alias=alias, check=check, field=field, spec=spec)

    def __init__(self, alias, check, field, spec):
        super().__init__(alias=alias, spec=spec)
        self.check = check
        self.field = field

    def apply(self, data):
        from ..types import Type
        field_type = Type.get(self.spec['schema'][self.field]['type'])
        if self.check not in data or data[self.check] is False:
            return self.field in data and not field_type.is_null(data[self.field])
        else:
            return True

    def get_params(self):
        return [self.check, self.field]
