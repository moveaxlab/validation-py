""" Array """
from .sequence import SequenceType
from ..constants import types
from ..exceptions import ArrayValidationError, ValidationError


class ArrayType(SequenceType):
    def __init__(self, spec: dict):
        """ Instantiate nested Type inside elements """
        from .type_factory import TypeFactory
        super().__init__(spec)
        if 'elements' in spec:
            self.nested_validation = True
            self.elements = TypeFactory.make(spec['elements'])

    @staticmethod
    def name() -> str:
        return types.ARRAY

    def validate(self, value):
        if not self.nested_validation:
            super().validate(value)
        else:
            if not self._validate_type(value):
                raise ValidationError(errors=[TypeError(self, value)])
            array_rule_errors = self._validate_rules(value)
            element_errors = []
            for element in value:
                try:
                    self.elements.validate(element)
                except ValidationError as element_exc:
                    element_errors.extend(element_exc.get_errors())
            if array_rule_errors or element_errors:
                raise ArrayValidationError(element_errors, array_rule_errors)

    @classmethod
    def _validate_type(cls, value) -> bool:
        if not super()._validate_type(value):
            return False
        return isinstance(value, (set, list))
