""" Nullable """
from .rule import Rule
from ..constants import rules
from ..types import Type


class NullableRule(Rule):
    required_params = 0
    supported_types = (Type,)

    @staticmethod
    def name() -> str:
        return rules.NULLABLE

    def _abides_by_the_rule(self, value) -> bool:
        raise NotImplementedError
