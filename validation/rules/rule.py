""" Rule """
from abc import ABC, abstractmethod
from typing import Iterable, List, Optional

from ..exceptions import RuleError, SpecError


class Rule(ABC):
    # Amount of params expected by the Rule. None disables check.
    required_params = None
    # Tuple of Types to which the rule applies
    supported_types = ()

    def __init__(self, type, alias: Optional[str] = None, params: Optional[List[str]] = None):
        # Set internal attributes
        self.alias = alias or self.name()
        self.params = params or []
        self.type = type
        # Validate rule
        self._check_type()
        self._check_params()

    def apply(self, value):
        """ Applies the rule to the value """
        if not self._abides_by_the_rule(value):
            raise RuleError(self, value)

    def get_failure_params(self, value) -> Iterable[str]:
        """ Getter for params on validation failure """
        return self.params

    @staticmethod
    @abstractmethod
    def name() -> str:
        """ Specifies the name of the rule """

    @abstractmethod
    def _abides_by_the_rule(self, value) -> bool:
        """ Check whether the value abides by the rule of not """

    def _check_params(self):
        """ Check the params are valid """
        if self.required_params is not None:
            if self.required_params != len(self.params):
                raise SpecError(f'The "{self.name()} rule expects {self.required_params} parameters."')
        try:
            self._sanitize_params()
        except SpecError as e:
            raise e
        except Exception:
            raise SpecError(f'The params {self.params} passed to the rule {self.name()} are invalid.')

    def _check_type(self):
        """ Check the type is supported """
        if not issubclass(self.type.__class__, self.supported_types):
            raise SpecError(f'The rule "{self.name()}" does not support the type {self.type.name()}')

    def _sanitize_params(self):
        """
        Check params are valid and cast them to the appropriate type.
        By default, nothing is done. But if a Rule requires it, this method should be overridden.
        """
