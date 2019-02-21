from decimal import Decimal

from .rule import Rule


class DecimalRule(Rule):

    @staticmethod
    def name():
        return 'decimal'

    def apply(self, data):
        try:
            Decimal(data)
            return True
        except Exception:
            return False
