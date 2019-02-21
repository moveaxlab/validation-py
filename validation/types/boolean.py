from .type import Type

from ..rules import MustBeTrueRule


class Boolean(Type):

    supported_rules = {MustBeTrueRule}

    @staticmethod
    def name():
        return 'boolean'

    @classmethod
    def check(cls, value):
        return isinstance(value, bool)
