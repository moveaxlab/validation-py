import re
from .string import String


class Base64(String):

    @staticmethod
    def name():
        return 'base64'

    @classmethod
    def check(cls, value):
        if not super(Base64, cls).check(value):
            return False
        regex = re.compile(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
        return regex.match(value) is not None
