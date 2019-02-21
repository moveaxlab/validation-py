from .rule import Rule

from ..utils.base64file_utils import get_size


class MaxSizeRule(Rule):

    @staticmethod
    def name():
        return 'max_size'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, maxsize=int(params_string), spec=spec)

    def __init__(self, alias, maxsize, spec):
        super().__init__(alias=alias, spec=spec)
        self.maxsize = maxsize

    def apply(self, data):
        return get_size(data) <= self.maxsize

    def get_params(self):
        return [self.maxsize]
