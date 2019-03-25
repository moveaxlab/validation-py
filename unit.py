import json
import os
from unittest import TestCase, main

from validation.constants import rules, types
from validation.exceptions import ArrayValidationError, ObjectValidationError, SpecError, ValidationError
from validation.parser import SpecParser
from validation.types.type_factory import TypeFactory
from validation.validator import ValidatorFactory

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = './validation-test-vectors/vectors.json'

with open('{}/{}'.format(dir_path, filename)) as infile:
    vectors = json.load(infile)


class TestTypes(TestCase):
    def test_all(self):
        for type_ in vectors['types']:
            for key, obj in vectors['types'][type_].items():
                spec = {"nullable": True, "rules": [], "type": type_}
                for value in obj:
                    if key == 'success':
                        self.assertTrue(TypeFactory.make(spec)._validate_type(value),
                                        'Type {} fails on {}'.format(type_, value))
                    elif key == 'failure':
                        self.assertFalse(TypeFactory.make(spec)._validate_type(value),
                                         'Type {} should have failed on {}'.format(type_, value))
                    else:
                        raise ValueError('Vector contained unknown key {}'.format(key))

    def test_array_without_nested_validation(self):
        value = [5]
        self.assertIsNone(ValidatorFactory.make({"rules": ["{}:1,3".format(rules.BETWEENLEN)],
                                                 "type": types.ARRAY}).validate(value))

    def test_object_without_nested_validation(self):
        value = {'a': 1, 'b': 1}
        self.assertIsNone(ValidatorFactory.make({"rules": ["{}:a,b".format(rules.EQUALS_TO)],
                                                 "type": types.OBJECT}).validate(value))

    def test_unknown_type(self):
        with self.assertRaises(SpecError, msg='Validator should not accept unknown types'):
            TypeFactory.make({"rules": [], "type": "unknown_type"})


def turn_lists_to_sets(errors):
    res = {}
    if not isinstance(errors, dict):
        return errors
    if 'name' in errors and 'params' in errors:
        return errors['name']
    for key, value in errors.items():
        if isinstance(value, list):
            value = [turn_lists_to_sets(x) for x in value]
            if all([not isinstance(x, dict) for x in value]):
                value = set(value)
        elif isinstance(value, dict):
            value = turn_lists_to_sets(value)
        res[key] = value
    return res


class TestValidators(TestCase):
    def test_all(self):
        for spec in vectors['specs']:
            validator = ValidatorFactory.make(spec['spec'])
            for data in spec['success']:
                self.assertIsNone(validator.validate(data))
            for data in spec['failure']:
                try:
                    with self.assertRaises(ValidationError):
                        validator.validate(data['data'])
                except ValidationError as e:
                    self.assertEqual(turn_lists_to_sets(data['failing']),
                                     turn_lists_to_sets(e.to_json()))

    # TODO: implement strict validation
    # def test_strict_validation(self):
    #     for spec in vectors['strict']:
    #         for data in spec['success']:
    #             validator = ValidatorFactory.make(spec['spec'])
    #             self.assertIsNone(validator.validate(data))
    #
    #         for data in spec['failure']:
    #             validator = ValidatorFactory.make(spec['spec'])
    #             try:
    #                 with self.assertRaises(ValidationError):
    #                     validator.validate(data['data'])
    #             except ValidationError as e:
    #                 self.assertEqual(turn_lists_to_sets(data['failing']),
    #                                  turn_lists_to_sets(e.to_json()))


class TestExceptions(TestCase):
    def test_array_validation_error_output(self):
        string_value = "some r4nd0m string"
        expected_output = {
            "elements_errors": [{"name": rules.ALPHA, "params": [], "value": string_value}],
            "errors": [{"name": rules.MINLEN, "params": ['3'], "value": [string_value]}]
        }
        try:
            ValidatorFactory.make({
                "elements": {"rules": [rules.ALPHA], "type": types.STRING},
                "rules": ["{}:3".format(rules.MINLEN)],
                "type": types.ARRAY}).validate([string_value])
        except ArrayValidationError as e:
            self.assertDictEqual(e.to_json(), expected_output)

    def test_object_validation_error_legacy_output_with_required_error(self):
        self.maxDiff = None
        string_value = "some r4nd0m string"
        value = {"a": string_value}
        expected_output = {
            "errors": [],
            "schema_errors": {
                "a": {
                    "errors": [{"name": rules.ALPHA, "params": [], "value": string_value}]
                },
                "b": {
                    "errors": [{"name": rules.REQUIRED, "params": "b", "value": None}]
                }
            }
        }
        try:
            ValidatorFactory.make({
                "rules": [],
                "schema": {
                    "a": {"rules": [rules.ALPHA], "type": types.STRING},
                    "b": {"rules": [rules.REQUIRED], "type": types.BOOLEAN}
                },
                "type": types.OBJECT}).validate(value)
        except ObjectValidationError as e:
            self.assertDictEqual(e.to_json(), expected_output)

    def test_object_validation_error_legacy_output_without_required_error(self):
        self.maxDiff = None
        string_value = "some r4nd0m string"
        value = {"a": string_value}
        expected_output = {
            "errors": [{"name": rules.EQUALS_TO, "params": ["a", "b"], "value": value}],
            "schema_errors": {
                "a": {"errors": [{"name": types.FLOAT, "value": string_value}]}
            }
        }
        try:
            ValidatorFactory.make({
                "rules": ["{}:a,b".format(rules.EQUALS_TO)],
                "schema": {
                    "a": {"rules": [], "type": types.FLOAT}
                },
                "type": types.OBJECT}).validate(value)
        except ObjectValidationError as e:
            self.assertDictEqual(e.to_json(), expected_output)


class TestRules(TestCase):
    def test_param_amount_check_rules(self):
        with self.assertRaises(SpecError, msg='AlphaRule should not accept parameters'):
            ValidatorFactory.make({"rules": "{}:param".format(rules.ALPHA), "type": types.STRING})

    def test_param_required_self_check_rules(self):
        rule_schema = {
            types.BASE64_ENCODED_FILE: rules.FILE_FORMAT,
            types.STRING: rules.IN}
        for type_, rule in rule_schema.items():
            with self.assertRaises(SpecError, msg='{} should expect parameters'.format(rule)):
                ValidatorFactory.make({"rules": rule, "type": type_})

    def test_one_numeric_param_rules(self):
        rule_schema = {
            types.FLOAT: [rules.MAX, rules.MIN],
            types.STRING: [rules.LEN, rules.MAXLEN, rules.MINLEN]}
        for type_, rules_ in rule_schema.items():
            for rule in rules_:
                with self.assertRaises(SpecError, msg='{} should accept only numeric parameters'.format(rule)):
                    ValidatorFactory.make({"rules": ["{}:param".format(rule)], "type": type_})

    def test_two_numeric_param_rules(self):
        rule_schema = {
            types.FLOAT: [rules.BETWEEN],
            types.STRING: [rules.BETWEENLEN]}
        for type_, rules_ in rule_schema.items():
            for rule in rules_:
                with self.assertRaises(SpecError, msg='{} should accept two numeric parameters'.format(rule)):
                    ValidatorFactory.make({"rules": ["{}:param1,param2".format(rule)], "type": type_})

    def test_betweenlen_rule_param_validation(self):
        with self.assertRaises(SpecError, msg='BetweenLenRule should accept only int-type parameters'):
            ValidatorFactory.make({"rules": ["{}:1,3.5".format(rules.BETWEENLEN)], "type": types.STRING})

    def test_len_rule_with_incorrect_params(self):
        with self.assertRaises(SpecError, msg='LenRule should accept only int-type params'):
            ValidatorFactory.make({"rules": ["{}:3.6".format(rules.LEN)], "type": types.STRING})

    def test_rule_not_supported_by_type(self):
        with self.assertRaises(SpecError, msg='Rules should check supported types'):
            ValidatorFactory.make({"rules": [rules.MUST_BE_TRUE], "type": types.ARRAY})

    def test_unknown_rule(self):
        with self.assertRaises(SpecError, msg='Validator should not accept unknown rules'):
            ValidatorFactory.make({"rules": ["unknown_rule:1,gd"], "type": types.OBJECT})

    def test_inherited_supported_types(self):
        self.assertIsNotNone(ValidatorFactory.make({"rules": [rules.ALPHANUM], "type": types.EMAIL}),
                             'The supported types are not inherited correctly.')


class TestSpecParser(TestCase):
    def test_nullable_rule_is_removed(self):
        parsed_ll_spec = SpecParser.parse({"rules": rules.NULLABLE, "type": types.INTEGER})
        self.assertListEqual(parsed_ll_spec['rules'], [], 'Nullable rule was not removed')

    def test_single_level_rules_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["{}:100,150".format(rules.BETWEEN), "{}:3".format(rules.MIN), rules.NULLABLE],
                                           "type": types.INTEGER})
        self.assertListEqual(parsed_ll_spec['rules'], [{'name': rules.BETWEEN, 'params': ['100', '150']},
                                                       {'name': rules.MIN, 'params': ['3']}],
                             'Single level rules parsed incorrectly')

    def test_nested_array_spec_rules_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["{}:100".format(rules.MAX), rules.NULLABLE], "type": types.ARRAY,
                                           "elements": {"rules": ["{}:100".format(rules.MAXLEN), rules.NULLABLE],
                                                        "type": types.STRING}})
        self.assertListEqual(parsed_ll_spec['elements']['rules'], [{'name': rules.MAXLEN, 'params': ['100']}],
                             'Nested array rules are not parsed correctly')

    def test_nested_object_spec_rules_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["{}:100".format(rules.MAX), rules.NULLABLE], "type": types.OBJECT,
                                           "schema": {"a": {"rules": ["{}:100".format(rules.MAXLEN), rules.NULLABLE],
                                                            "type": types.STRING}}})
        self.assertListEqual(parsed_ll_spec['schema']['a']['rules'], [{'name': rules.MAXLEN, 'params': ['100']}],
                             'Nested object rules are not parsed correctly')

    def test_parsing_incorrect_rule_format(self):
        with self.assertRaises(SpecError, msg='The parser incorrectly accepted a rule'):
            SpecParser.parse({"rules": ["{}<123>".format(rules.BETWEEN)], "type": types.STRING})

    def test_parsing_no_rules_submitted(self):
        with self.assertRaises(SpecError, msg='The key "rules" is required.'):
            SpecParser.parse({"type": types.STRING})

    def test_parsing_no_type_submitted(self):
        with self.assertRaises(SpecError, msg='The key "type" is required.'):
            SpecParser.parse({"rules": "{}:10|{}".format(rules.MAX, rules.NULLABLE)})

    def test_alias_usage(self):
        alias = 'some_alias'
        parsed_ll_spec = SpecParser.parse({"rules": "{}[{}]:10|{}".format(rules.MAXLEN, alias, rules.NULLABLE),
                                           "type": types.STRING})
        self.assertEqual(parsed_ll_spec['rules'][0]['alias'], alias)

    def test_parsing_incorrect_elements_usage(self):
        with self.assertRaises(SpecError, msg='Only "array" structures must define "elements"'):
            SpecParser.parse({"elements": {"rules": ["{}:100".format(rules.MAXLEN)], "type": types.STRING},
                              "rules": ["{}:100".format(rules.MAXLEN), rules.NULLABLE], "type": types.STRING})

    def test_parsing_incorrect_schema_usage(self):
        with self.assertRaises(SpecError, msg='Only "object" structures must define a "schema"'):
            SpecParser.parse({"rules": ["{}:100".format(rules.MAXLEN), rules.NULLABLE], "type": types.STRING,
                              "schema": {"a": {"rules": ["{}:100".format(rules.MAXLEN)], "type": types.STRING}}})

    def test_required_rule_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": [rules.NULLABLE], "type": types.OBJECT,
                                           "schema": {"a": {"rules": [rules.REQUIRED, rules.NULLABLE],
                                                            "type": types.STRING},
                                                      "b": {"rules": [rules.NULLABLE], "type": types.STRING},
                                                      "c": {"rules": "{}|{}".format(rules.REQUIRED, rules.NULLABLE),
                                                            "type": types.FLOAT}}})
        self.assertEqual(parsed_ll_spec['rules'][-1]['name'],
                         'required', 'Required is not a top level rule')
        self.assertSetEqual(set(parsed_ll_spec['rules'][-1]['params']),
                            set(["a", "c"]), 'Not all required keys are listed')

    def test_whole_parsing_example(self):
        self.maxDiff = None
        with open(os.path.join(dir_path, 'test', 'hl_spec.json')) as hl_spec_file:
            hl_spec = json.load(hl_spec_file)
        with open(os.path.join(dir_path, 'test', 'll_spec.json')) as ll_spec_file:
            ll_spec = json.load(ll_spec_file)
        parsed_ll_spec = SpecParser.parse(hl_spec)
        self.assertDictEqual(turn_lists_to_sets(ll_spec), turn_lists_to_sets(parsed_ll_spec))


if __name__ == '__main__':
    main()
