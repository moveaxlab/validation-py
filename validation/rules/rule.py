import re
from abc import ABCMeta, abstractmethod

from ..exceptions import UnknownRule


class IRule(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def name():
        """Specifies the name of the rule"""

    @classmethod
    @abstractmethod
    def parse(cls, alias, spec, params_string):
        """Creates the rule from a descriptive string"""

    @abstractmethod
    def apply(self, data):
        """Applies the rule to the data"""


class ARule(IRule, metaclass=ABCMeta):
    pass


class Rule(ARule, metaclass=ABCMeta):

    NAME_PARAM_SEP = ':'
    PARAMS_SEP = ','
    ALIAS_RE = re.compile(r"""
        ^                               # beginning of string
        (?P<name>\w+)                   # group the rule name
        (?:\[                           # if present, detect an alias between square brackets
            (?P<alias>[^\]]+)           # group the alias
        \])?
        $                               # end of string
    """, re.VERBOSE)
    RULE_FMT = 'name[alias]{}param1{}param2{}param3'.format(NAME_PARAM_SEP, PARAMS_SEP, PARAMS_SEP)

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, spec=spec)

    @classmethod
    def create(cls, desc, spec):
        from . import rules

        name, *params = desc.split(cls.NAME_PARAM_SEP, maxsplit=1)
        match = cls.ALIAS_RE.fullmatch(name)
        if match is not None:
            name = match.group('name')
            if match.group('alias') is not None:
                alias = match.group('alias')
            else:
                alias = name
        else:
            raise ValueError('Rule "{}" has wrong format. '
                             'Rules must have the following format: {}'.format(desc, cls.RULE_FMT))

        params = params[0] if params else None

        try:
            return rules[name].parse(alias, spec, params)
        except KeyError:
            raise UnknownRule('No rule found with name {}'.format(name))

    def __init__(self, alias, spec):
        self.alias = alias
        self.spec = spec

    def get_params(self):
        return []
