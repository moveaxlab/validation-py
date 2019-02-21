from .sequence import Sequence

from ..rules import AlphaNumRule, AlphaRule, AlphaDashRule, DecimalRule, HexRule, RegexRule


class String(Sequence):

    supported_rules = {AlphaNumRule, AlphaRule, AlphaDashRule, DecimalRule, HexRule, RegexRule}
    null_values = ['']

    @staticmethod
    def name():
        return 'string'

    @classmethod
    def check(cls, value):
        if not super(String, cls).check(value):
            return False
        return isinstance(value, str)
