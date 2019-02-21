import re
from .string import String


class Base58(String):

    @staticmethod
    def name():
        return 'base58'

    @classmethod
    def check(cls, value):
        if not super(Base58, cls).check(value):
            return False
        regex = re.compile(r'^[1-9A-HJ-NP-Za-km-z]+$')
        return regex.match(value) is not None
