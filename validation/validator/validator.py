from abc import ABCMeta, abstractmethod

from ..rules import RuleSet, NullableRule
from ..types import Type
from ..exceptions import SpecError
from .validator_error import ValidatorError
from .validator_summary import ValidatorSummary


class IValidator(metaclass=ABCMeta):

    @abstractmethod
    def validate(self, data, strict=False):
        raise NotImplemented()


class AValidator(IValidator, metaclass=ABCMeta):
    def __init__(self, schema):
        self.schema = schema
        self.errors = ValidatorSummary()

    def _is_nullable(self):
        rules = self.schema['rules']
        if isinstance(rules, str):
            rules = rules.split('|')
        return NullableRule.name() in rules

    def validate(self, data, strict=False):
        self.errors.empty()

        schema = self.schema
        param_type = Type.get(schema['type'])

        rules = RuleSet.from_description(schema['rules'], schema)

        if not param_type.supports(rules):
            raise SpecError('Some specified rules not supported by type {}'.format(param_type.name()))

        if param_type.is_null(data):
            if self._is_nullable():
                return True
            else:
                self.errors.add_error(ValidatorError(NullableRule.name(), []))
                return False

        if not param_type.check(data):
            self.errors.add_error(ValidatorError('type', [param_type.name()]))
            return False

        success = True

        for rule in rules:
            if not rule.apply(data):
                success = False
                self.errors.add_error(ValidatorError(rule.alias, rule.get_params()))

        return success
