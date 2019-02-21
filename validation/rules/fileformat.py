from .rule import Rule

from ..utils.base64file_utils import get_format


class FileFormatRule(Rule):

    @staticmethod
    def name():
        return 'file_format'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, formats=params_string.split(','), spec=spec)

    def __init__(self, alias, formats, spec):
        super().__init__(alias=alias, spec=spec)
        self.formats = formats

    def apply(self, data):
        return get_format(data) in self.formats

    def get_params(self):
        return [",".join(self.formats)]
