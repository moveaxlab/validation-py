import phonenumbers
import re
from .string import String


class Phone(String):

    @staticmethod
    def name():
        return 'phone'

    @classmethod
    def check(cls, value):
        if not super().check(value):
            return False
        regex = re.compile(r'^\s*\+(\s*\(?\d\)?-?)*\s*$')
        if regex.match(value) is None:
            return False
        try:
            number = phonenumbers.parse(value, None)
        except phonenumbers.NumberParseException:
            return False
        return phonenumbers.is_valid_number(number)
