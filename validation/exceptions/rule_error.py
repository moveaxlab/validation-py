""" RuleError """
from .base_error import BaseError


class RuleError(BaseError):
    """ Error that occurs on Rule validation """
    def __init__(self, rule, value):
        self.params = rule.get_failure_params(value)
        self.rule_name = rule.name()
        self.value = value

    def __str__(self):
        if self.params:
            self.msg = f'{self.value} does not abide by the rule {self.rule_name} with params {self.params}'
        else:
            self.msg = f'{self.value} does not abide by the rule {self.rule_name}'

    @staticmethod
    def name() -> str:
        return 'RuleError'

    def to_json(self) -> dict:
        return {
            'name': self.rule_name,
            'params': self.params,
            'value': self.value
        }
