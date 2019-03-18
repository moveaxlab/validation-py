""" Alpha Num """
from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import StringType


class AlphaNumRule(Rule):
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.ALPHANUM

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value has non alphanumeric characters.
        return value.isalnum()

    def _sanitize_params(self):
        if self.params:
            raise SpecError(f'The AlphaNumRule takes no parameters')
