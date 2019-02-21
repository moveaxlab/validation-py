from .type import Type

from ..rules import EqualsToRule, NullableIfRule, OperationalFieldRule


class Object(Type):

    supported_rules = {EqualsToRule, NullableIfRule, OperationalFieldRule}
    null_values = [{}]

    @staticmethod
    def name():
        return 'object'

    @classmethod
    def check(cls, value):
        return isinstance(value, dict)
