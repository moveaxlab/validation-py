""" Rule Factory """
from typing import List, Optional

from . import rules, Rule
from ..exceptions import SpecError
from ..types import Type


class RuleFactory:
    @staticmethod
    def make(name: str, type: Type, alias: Optional[str] = None, params: Optional[List[str]] = None) -> Rule:
        """ Return a Rule based on the spec """
        try:
            rule = rules[name]
        except KeyError as e:
            raise SpecError('Unknown rule "{}"'.format(e.args[0]))
        return rule(alias=alias, params=params, type=type)
