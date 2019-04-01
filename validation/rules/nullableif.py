""" Nullable If """
from .rule import Rule
from ..constants import rules
from ..types import ObjectType


class NullableIfRule(Rule):
    required_params = 2
    supported_types = (ObjectType,)

    @staticmethod
    def name() -> str:
        return rules.NULLABLE_IF

    def _abides_by_the_rule(self, value: dict) -> bool:
        # Fail when the value in the target key is NULL and the value in the check key is not True.
        target_type = self.type.schema[self.target]
        if self.check not in value or value[self.check] is False:
            return self.target in value and not target_type.is_null(value[self.target])
        else:
            return True

    def _sanitize_params(self):
        self.check, self.target = self.params
