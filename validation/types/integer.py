from .float import Float


class Integer(Float):

    @staticmethod
    def name():
        return 'integer'

    @classmethod
    def check(cls, value):
        if not super(Integer, cls).check(value):
            return False
        return isinstance(value, int)
