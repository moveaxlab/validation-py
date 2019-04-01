""" RuleError """
from .base_error import BaseError


class RuleError(BaseError):
    """ Error that occurs on Rule validation """
    def __init__(self, rule, value):
        self.params = rule.get_failure_params(value)
        self.rule_name = rule.get_alias()
        self.value = value

    def __str__(self):
        if self.params:
            self.msg = '{} does not abide by the rule {} with params {}'.format(self.value, self.rule_name, self.params)
        else:
            self.msg = '{} does not abide by the rule {}'.format(self.value, self.rule_name)

    @staticmethod
    def name() -> str:
        return 'RuleError'

    def to_json(self) -> dict:
        return {
            'name': self.rule_name,
            'params': self.params,
            'value': self.value
        }
