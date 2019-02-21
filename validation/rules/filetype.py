from .rule import Rule

from ..utils.base64file_utils import get_type


class FileTypeRule(Rule):

    @staticmethod
    def name():
        return 'file_type'

    @classmethod
    def parse(cls, alias, spec, params_string):
        return cls(alias=alias, file_type=params_string, spec=spec)

    def __init__(self, alias, file_type, spec):
        super().__init__(alias=alias, spec=spec)
        self.type = file_type

    def apply(self, data):
        return get_type(data) == self.type

    def get_params(self):
        return [self.type]
