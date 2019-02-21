from .type import Type
from ..rules import MinRule, MaxRule, BetweenRule


class Float(Type):

    supported_rules = {MinRule, MaxRule, BetweenRule}

    @staticmethod
    def name():
        return 'float'

    @classmethod
    def check(cls, value):
        return isinstance(value, float) or isinstance(value, int)
