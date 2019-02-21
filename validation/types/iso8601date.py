from dateutil.parser import isoparse

from .string import String


class ISO_8601_Date(String):

    @staticmethod
    def name():
        return 'ISO_8601_date'

    @classmethod
    def check(cls, value):
        if not super(ISO_8601_Date, cls).check(value):
            return False
        try:
            isoparse(value)
            return True
        except ValueError:
            return False
