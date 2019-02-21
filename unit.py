import os
import json
from unittest import TestCase, main

from validation.types import Type

from validation.validator import ValidatorFactory

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = './vectors.json'

with open('{}/{}'.format(dir_path, filename)) as infile:
    vectors = json.load(infile)


class TestCustomRules(TestCase):
    def spec(self):
        return {
            "type": "object",
            "rules": ["operational_field_tmp_rule:a,b"],
            "schema": {
                "a": {
                    "type": "string",
                    "rules": [],
                },
                "b": {
                    "type": "string",
                    "rules": ["nullable"],
                },
            },
        }

    def test_other_not_null_is_valid(self):
        validator = ValidatorFactory.make(self.spec())
        data = {
            "a": "other",
            "b": "not null",
        }
        self.assertTrue(validator.validate(data))

    def test_other_null_is_not_valid(self):
        validator = ValidatorFactory.make(self.spec())
        data = {
            "a": "other",
            "b": None,
        }
        self.assertFalse(validator.validate(data))

    def test_something_null_is_valid(self):
        validator = ValidatorFactory.make(self.spec())
        data = {
            "a": "something",
            "b": None,
        }
        self.assertTrue(validator.validate(data))

    def test_something_not_null_is_not_valid(self):
        validator = ValidatorFactory.make(self.spec())
        data = {
            "a": "something",
            "b": "not null",
        }
        self.assertFalse(validator.validate(data))


class TestTypes(TestCase):

    def test_all(self):
        for type_ in vectors['types']:
            for key, obj in vectors['types'][type_].items():
                for value in obj:
                    if key == 'success':
                        self.assertTrue(Type.get(type_).check(value),
                                        'Type {} fails on {}'.format(type_, value))
                    elif key == 'failure':
                        self.assertFalse(Type.get(type_).check(value),
                                         'Type {} should have failed on {}'.format(type_, value))
                    else:
                        raise ValueError('Vector contained unknown key {}'.format(key))


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
            for data in spec['success']:
                validator = ValidatorFactory.make(spec['spec'])
                self.assertTrue(validator.validate(data))

            for data in spec['failure']:
                validator = ValidatorFactory.make(spec['spec'])
                self.assertFalse(validator.validate(data['data']))

                self.assertEqual(turn_lists_to_sets(data['failing']),
                                 turn_lists_to_sets(validator.errors.to_dict()))

    def test_strict_validation(self):
        for spec in vectors['strict']:
            for data in spec['success']:
                validator = ValidatorFactory.make(spec['spec'])
                self.assertTrue(validator.validate(data), True)

            for data in spec['failure']:
                validator = ValidatorFactory.make(spec['spec'])
                self.assertTrue(validator.validate(data['data'], False))
                self.assertFalse(validator.validate(data['data'], True))

                self.assertEqual(turn_lists_to_sets(data['failing']),
                                 turn_lists_to_sets(validator.errors.to_dict()))


if __name__ == '__main__':
    main()
