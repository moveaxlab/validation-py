""" Composite Type """
from .type import Type
from ..constants import types
from ..exceptions import ObjectValidationError, ValidationError


class CompositeType(Type):
    null_values = [{}]

    def __init__(self, spec: dict):
        """ Instantiate nested Types inside the schema """
        from .type_factory import TypeFactory
        super().__init__(spec)
        if 'schema' in spec:
            self.nested_validation = True
            self.schema = {key: TypeFactory.make(nested_spec) for key, nested_spec in spec['schema'].items()}

    @staticmethod
    def name() -> str:
        return types.COMPOSITE

    def validate(self, value):
        if not self.nested_validation:
            super().validate(value)
        else:
            if not self._validate_type(value):
                raise ValidationError(errors=[TypeError(self, value)])
            object_rule_errors = self._validate_rules(value)
            schema_errors = []
            for k, v in value.items():
                try:
                    self.schema[k].validate(v)
                except ValidationError as key_exc:
                    schema_errors.extend(key_exc.get_errors())
            if object_rule_errors or schema_errors:
                raise ObjectValidationError(object_rule_errors, schema_errors)

    @classmethod
    def _validate_type(cls, value) -> bool:
        return hasattr(value, '__getitem__')
