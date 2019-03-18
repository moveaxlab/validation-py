""" Required """
from .rule import Rule
from ..constants import rules
from ..types import ObjectType


class RequiredRule(Rule):
    supported_types = (ObjectType,)

    def get_failure_params(self, value) -> set:
        return self.params - value.keys()

    @staticmethod
    def name() -> str:
        return rules.REQUIRED

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when a key is not present inside the dict 'value'
        for param in self.params:
            if param not in value:
                return False
        return True
