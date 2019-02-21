from validation.types import Array
from .array_validator_summary import ArrayValidatorSummary
from .validator import AValidator
from .validator_factory import ValidatorFactory

class ArrayValidator(AValidator):
    def __init__(self, schema):
        super(ArrayValidator, self).__init__(schema)
        self.errors = ArrayValidatorSummary()

    def validate(self, data, strict=False):
        success = super(ArrayValidator, self).validate(data, strict)

        if not Array.check(data) or Array.is_null(data):
            return success

        validator = ValidatorFactory.make(self.schema['elements'])

        for element in data:
            valid = validator.validate(element, strict)

            if not valid:
                success = False

            self.errors.add_elements_errors([validator.errors])

        return success