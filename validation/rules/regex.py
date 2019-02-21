import re

from .rule import Rule


class RegexRule(Rule):

    @staticmethod
    def name():
        return 'regex'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, regex=params_string, spec=spec)

    def __init__(self, alias, regex, spec):
        super().__init__(alias=alias, spec=spec)
        self.regex = re.compile(regex)

    def apply(self, data):
        match = self.regex.search(data)
        return match is not None

    def get_params(self):
        return [self.regex.pattern]
