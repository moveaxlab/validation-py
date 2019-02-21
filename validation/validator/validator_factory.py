
class ValidatorFactory(object):
    @staticmethod
    def make(schema):
        from .array_validator import ArrayValidator
        from .object_validator import ObjectValidator
        from .primitive_validator import PrimitiveValidator
        if schema['type'] == 'object':
            return ObjectValidator(schema)
        elif schema['type'] == 'array':
            return ArrayValidator(schema)
        else:
            return PrimitiveValidator(schema)
