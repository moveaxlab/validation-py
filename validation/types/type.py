""" Type """
from abc import ABCMeta, abstractmethod
from typing import List

from ..exceptions import NullableError, RuleError, TypeError, ValidationError


class MetaType(ABCMeta):
    def __new__(mcs, name, bases, dct):
        # Child class extends the parent's null_values
        if 'null_values' not in dct:
            dct['null_values'] = []
        for base in bases:
            for null_value in base.null_values:
                dct['null_values'].append(null_value)
        return super().__new__(mcs, name, bases, dct)


class Type(metaclass=MetaType):
    # Should validate nested types?
    nested_validation = False
    # List of NULL equivalent values for the Type
    null_values = [None]

    def __init__(self, spec: dict):
        from ..rules.rule_factory import RuleFactory
        self.nullable = spec['nullable']
        self.rules = [RuleFactory.make(type=self, **rule) for rule in spec['rules']]

    @classmethod
    def is_null(cls, value) -> bool:
        """ Check whether the value is null or not """
        return value in cls.null_values

    @staticmethod
    @abstractmethod
    def name() -> str:
        """ Specifies the name of the type """

    def validate(self, value):
        """ Validate the value type and apply the rules """
        if self.is_null(value):
            if not self.nullable:
                raise ValidationError(errors=[NullableError(value)])
        else:
            if not self._validate_type(value):
                raise ValidationError(errors=[TypeError(self, value)])
            rule_errors = self._validate_rules(value)
            if rule_errors:
                raise ValidationError(errors=rule_errors)

    def _validate_rules(self, value) -> List[RuleError]:
        """ Validate the value against the rules """
        rule_errors = []
        for rule in self.rules:
            try:
                rule.apply(value)
            except RuleError as e:
                rule_errors.append(e)
        return rule_errors

    @classmethod
    @abstractmethod
    def _validate_type(cls, value) -> bool:
        """ Validate the value type """
