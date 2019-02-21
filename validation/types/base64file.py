import re

from .string import String

from ..rules import FileFormatRule, FileTypeRule, MaxSizeRule, MinSizeRule


class Base64EncodedFile(String):

    supported_rules = {FileFormatRule, FileTypeRule, MaxSizeRule, MinSizeRule}

    @staticmethod
    def name():
        return 'base64_encoded_file'

    @classmethod
    def check(cls, value):
        if not super(Base64EncodedFile, cls).check(value):
            return False
        regex = re.compile(
            r'^'
            r'data:[a-z]+/[a-z]+;base64,'
            r'(?:[A-Za-z0-9+/]{4})*'
            r'(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
            r'$'
        )
        return regex.match(value) is not None
