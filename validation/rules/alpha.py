""" Alpha """
from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import StringType


class AlphaRule(Rule):
    supported_types = (StringType,)

    @staticmethod
    def name() -> str:
        return rules.ALPHA

    def _abides_by_the_rule(self, value: str) -> bool:
        # Fail when the value has non alphabetic characters.
        return value.isalpha()

    def _sanitize_params(self):
        if self.params:
            raise SpecError(f'The AlphaRule takes no parameters')
