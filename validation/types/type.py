from abc import ABCMeta, abstractmethod

from ..rules import EqualsRule, InRule, RequiredRule, NullableRule


class MetaType(ABCMeta):

    def __new__(cls, name, bases, dct):

        if 'supported_rules' not in dct:
            dct['supported_rules'] = set()

        if 'null_values' not in dct:
            dct['null_values'] = []

        for base in bases:
            for rule in base.supported_rules:
                dct['supported_rules'].add(rule)
            for null_value in base.null_values:
                dct['null_values'].append(null_value)

        return super().__new__(cls, name, bases, dct)


class Type(metaclass=MetaType):

    supported_rules = {EqualsRule, InRule, NullableRule, RequiredRule}
    null_values = [None]

    @staticmethod
    @abstractmethod
    def name():
        """Defines the name by which the type is identified"""

    @classmethod
    @abstractmethod
    def check(cls, value):
        """Checks whether the value belongs to the defining type"""

    @classmethod
    def is_null(cls, value):
        return value in cls.null_values

    @classmethod
    def supports(cls, ruleset):
        for rule in ruleset:
            if rule.__class__ not in cls.supported_rules:
                return False
        return True

    @staticmethod
    def get(type_name):
        from . import types

        try:
            return types[type_name]
        except KeyError:
            raise ValueError('Unknown type {}'.format(type_name))
