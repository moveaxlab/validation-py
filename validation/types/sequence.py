from .type import Type

from ..rules import MinLengthRule, MaxLengthRule, BetweenLengthRule, LengthRule


class Sequence(Type):

    supported_rules = {MinLengthRule, MaxLengthRule, BetweenLengthRule, LengthRule}
    null_values = [[]]

    @staticmethod
    def name():
        return 'sequence'

    @classmethod
    def check(cls, value):
        return hasattr(value, '__iter__')
