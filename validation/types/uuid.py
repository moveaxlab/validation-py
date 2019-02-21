from .string import String
from uuid import UUID as create_uuid


class UUID(String):

    @staticmethod
    def name():
        return 'uuid'

    @classmethod
    def check(cls, value):
        if not super(UUID, cls).check(value):
            return False
        try:
            created = create_uuid(str(value), version=4)
        except ValueError:
            return False
        return value == str(created)
