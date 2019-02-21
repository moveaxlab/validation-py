from .rule import Rule

from ..utils.base64file_utils import get_size


class MinSizeRule(Rule):

    @staticmethod
    def name():
        return 'min_size'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, minsize=int(params_string), spec=spec)

    def __init__(self, alias, minsize, spec):
        super().__init__(alias=alias, spec=spec)
        self.minsize = minsize

    def apply(self, data):
        return get_size(data) >= self.minsize

    def get_params(self):
        return [self.minsize]
