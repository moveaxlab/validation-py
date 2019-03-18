""" Must Be True """
from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import BooleanType


class MustBeTrueRule(Rule):
    supported_types = (BooleanType,)

    @staticmethod
    def name() -> str:
        return rules.MUST_BE_TRUE

    def _abides_by_the_rule(self, value) -> bool:
        # Fail if value is Falsy
        return value is True

    def _sanitize_params(self):
        if self.params:
            raise SpecError(f'The MustBeTrueRule takes no parameters')
