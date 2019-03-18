import json
import os
from unittest import TestCase, main

from validation.exceptions import SpecError, ValidationError
from validation.parser import SpecParser
from validation.types.type_factory import TypeFactory
from validation.validator import ValidatorFactory

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = './validation-test-vectors/vectors.json'

with open(f'{dir_path}/{filename}') as infile:
    vectors = json.load(infile)


class TestTypes(TestCase):
    def test_all(self):
        for type_ in vectors['types']:
            for key, obj in vectors['types'][type_].items():
                spec = {"nullable": True, "rules": [], "type": type_}
                for value in obj:
                    if key == 'success':
                        self.assertTrue(TypeFactory.make(spec)._validate_type(value),
                                        f'Type {type_} fails on {value}')
                    elif key == 'failure':
                        self.assertFalse(TypeFactory.make(spec)._validate_type(value),
                                         f'Type {type_} should have failed on {value}')
                    else:
                        raise ValueError(f'Vector contained unknown key {key}')


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


class TestSpecParser(TestCase):
    def test_nullable_rule_is_removed(self):
        parsed_ll_spec = SpecParser.parse({"rules": ['nullable'], "type": "integer"})
        self.assertListEqual(parsed_ll_spec['rules'], [], 'Nullable rule was not removed')

    def test_not_null_rule_is_added(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["max:100"], "type": "integer"})
        self.assertListEqual(parsed_ll_spec['rules'], [{'name': 'max', 'params': ['100']}],
                             'Not_null rule was not added')

    def test_single_level_rules_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["between:100,150", "min:3", "nullable"], "type": "integer"})
        self.assertListEqual(parsed_ll_spec['rules'], [{'name': 'between', 'params': ['100', '150']},
                                                       {'name': 'min', 'params': ['3']}],
                             'Single level rules parsed incorrectly')

    def test_nested_array_spec_rules_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["max:100", "nullable"], "type": "array",
                                           "elements": {"rules": ["maxlen:100", "nullable"], "type": "string"}})
        self.assertListEqual(parsed_ll_spec['elements']['rules'], [{'name': 'maxlen', 'params': ['100']}],
                             'Nested array rules are not parsed correctly')

    def test_nested_object_spec_rules_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["max:100", "nullable"], "type": "object",
                                           "schema": {"a": {"rules": ["maxlen:100", "nullable"], "type": "string"}}})
        self.assertListEqual(parsed_ll_spec['schema']['a']['rules'], [{'name': 'maxlen', 'params': ['100']}],
                             'Nested object rules are not parsed correctly')

    def test_parsing_no_rules_submitted(self):
        with self.assertRaises(SpecError, msg='The key "rules" is required.'):
            SpecParser.parse({"type": "string"})

    def test_parsing_no_type_submitted(self):
        with self.assertRaises(SpecError, msg='The key "type" is required.'):
            SpecParser.parse({"rules": "max:10|nullable"})

    def test_parsing_incorrect_elements_usage(self):
        with self.assertRaises(SpecError, msg='Only "array" structures must define "elements"'):
            SpecParser.parse({"rules": ["maxlen:100", "nullable"], "type": "string",
                              "schema": {"a": {"rules": ["maxlen:100"], "type": "string"}}})

    def test_parsing_incorrect_schema_usage(self):
        with self.assertRaises(SpecError, msg='Only "object" structures must define a "schema"'):
            SpecParser.parse({"rules": ["maxlen:100", "nullable"], "type": "string",
                              "schema": {"a": {"rules": ["maxlen:100"], "type": "string"}}})

    def test_required_rule_parsing(self):
        parsed_ll_spec = SpecParser.parse({"rules": ["nullable"], "type": "object",
                                           "schema": {"a": {"rules": "required|nullable", "type": "string"},
                                                      "b": {"rules": ["nullable"], "type": "string"},
                                                      "c": {"rules": "required|nullable", "type": "float"}}})
        self.assertEqual(parsed_ll_spec['rules'][-1]['name'],
                         'required', 'Required is not a top level rule')
        self.assertEqual(parsed_ll_spec['rules'][-1]['params'],
                         ["a", "c"], 'Not all required keys are listed')

    def test_whole_parsing_example(self):
        self.maxDiff = None
        with open(os.path.join(dir_path, 'test', 'hl_spec.json')) as hl_spec_file:
            hl_spec = json.load(hl_spec_file)
        with open(os.path.join(dir_path, 'test', 'll_spec.json')) as ll_spec_file:
            ll_spec = json.load(ll_spec_file)
        parsed_ll_spec = SpecParser.parse(hl_spec)
        self.assertDictEqual(ll_spec, parsed_ll_spec)


if __name__ == '__main__':
    main()
