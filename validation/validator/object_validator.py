from validation.rules import RequiredRule
from validation.types import Object
from .validator_error import ValidatorError
from .object_validator_summary import ObjectValidatorSummary
from .validator import AValidator
from .validator_factory import ValidatorFactory


class ObjectValidator(AValidator):
    def __init__(self, schema):
        super(ObjectValidator, self).__init__(schema)
        self.errors = ObjectValidatorSummary()

    def _is_required(self, key):
        rules = self.schema['schema'][key]['rules']
        if isinstance(rules, str):
            rules = rules.split('|')
        return RequiredRule.name() in rules


    def validate(self, data, strict=False):
        success = super(ObjectValidator, self).validate(data, strict)

        if not Object.check(data) or (Object.is_null(data) and self._is_nullable()):
            return success

        schema = self.schema['schema']
        for key, desc in schema.items():
            if key not in data:
                if self._is_required(key):
                    self.errors.add_schema_error(key, ValidatorError(RequiredRule.name(), []))
                    success = False
            else:
                validator = ValidatorFactory.make(schema[key])
                valid = validator.validate(data[key], strict)
                if not valid:
                    success = False
                    self.errors.add_schema_errors(key, validator.errors)

        if strict:
            for key in data:
                if key not in schema:
                    success = False
                    self.errors.add_schema_error(key, ValidatorError('strict', []))

        return success
