import re

from decimal import Decimal

from .rule import Rule


class DecimalRule(Rule):

    @staticmethod
    def name():
        return 'decimal'

    def apply(self, data):
        if re.match('^\d{1,21}(\.\d{1,2})?$', data) is None:
            return False
        try:
            Decimal(data)
            return True
        except Exception:
            return False
