""" Required """
from .rule import Rule
from ..constants import rules
from ..types import ObjectType


class RequiredRule(Rule):
    supported_types = (ObjectType,)

    def get_failure_params(self, value) -> list:
        return list(self.keys - value.keys())

    @staticmethod
    def name() -> str:
        return rules.REQUIRED

    def _abides_by_the_rule(self, value: dict) -> bool:
        # Fail when a key is not present inside the dict 'value'
        return all(key in value for key in self.keys)

    def _sanitize_params(self):
        self.keys = self.params
