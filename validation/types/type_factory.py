""" Type Factory """
from . import Type, types
from ..exceptions import SpecError


class TypeFactory:
    @staticmethod
    def make(spec: dict) -> Type:
        """ Return a Type wrapper of the whole spec """
        try:
            type_validator = types[spec['type']]
        except KeyError as e:
            raise SpecError(f'Unknown type "{e.args[0]}"')
        return type_validator(spec)
