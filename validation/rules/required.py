""" Required """
from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import ObjectType


class RequiredRule(Rule):
    supported_types = (ObjectType,)

    def get_failure_params(self, value) -> set:
        return self.keys - value.keys()

    @staticmethod
    def name() -> str:
        return rules.REQUIRED

    def _abides_by_the_rule(self, value: dict) -> bool:
        # Fail when a key is not present inside the dict 'value'
        return all(key in value for key in self.keys)

    def _sanitize_params(self):
        if not self.params:
            raise SpecError(f'At least one file format is required')
        self.keys = self.params
