""" Is In """
from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import Type


class InRule(Rule):
    supported_types = (Type,)

    @staticmethod
    def name() -> str:
        return rules.IN

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the value is not equal to any of the targets.
        return str(value) in self.targets

    def _sanitize_params(self):
        if not self.params:
            raise SpecError('At least one parameter is required')
        self.targets = self.params
