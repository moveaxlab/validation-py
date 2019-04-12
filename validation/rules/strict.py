""" Strict """
from .rule import Rule
from ..constants import rules
from ..types import ObjectType


class StrictRule(Rule):
    required_params = 0
    supported_types = (ObjectType,)

    def get_failure_params(self, value) -> list:
        return list(value.keys() - self.type.schema.keys())

    @staticmethod
    def name() -> str:
        return rules.STRICT

    def _abides_by_the_rule(self, value: dict) -> bool:
        # Skip strictness check if schema is undeclared
        if not hasattr(self.type, 'schema'):
            return True
        # Fail when the value has keys undeclared on the schema
        return all(key in self.type.schema.keys() for key in value.keys())
