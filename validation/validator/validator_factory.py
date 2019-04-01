""" Validator Factory """
from ..parser import SpecParser
from ..types.type_factory import Type, TypeFactory


class ValidatorFactory:
    @staticmethod
    def make(spec: dict) -> Type:
        """ Parse the spec and return a Type wrapper """
        ll_spec = SpecParser.parse(spec)
        return TypeFactory.make(ll_spec)
