from .sequence import Sequence


class Array(Sequence):

    @staticmethod
    def name():
        return 'array'

    @classmethod
    def check(cls, value):
        if not super(Array, cls).check(value):
            return False
        return isinstance(value, (set, list))
