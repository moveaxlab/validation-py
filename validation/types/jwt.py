""" JWT (JSON Web Token) """
from . import CompositeType
from ..constants import types


class JWTType(CompositeType):
    @staticmethod
    def name() -> str:
        return types.JWT

    @staticmethod
    def _validate_type(value) -> bool:
        if not super()._validate_type(value):
            return False
        raise NotImplementedError
