""" Spec Parser """
import re

from ..constants import rules, types
from ..exceptions import SpecError

# Constants
ALIAS_RE = re.compile(r"""
    ^                               # beginning of string
    (?P<name>\w+)                   # group the rule name
    (?:\[                           # if present, detect an alias between square brackets
        (?P<alias>[^\]]+)           # group the alias
    \])?
    $                               # end of string
""", re.VERBOSE)
NAME_PARAM_SEP = ':'
PARAMS_SEP = ','
RULE_FMT = 'name[alias]{}param1{}param2{}param3'.format(NAME_PARAM_SEP, PARAMS_SEP, PARAMS_SEP)
RULE_SEP = '|'


class SpecParser:
    @classmethod
    def parse(cls, hl_spec: dict, strict: bool) -> dict:
        """ Parse a high-level spec into a low-level spec """
        try:
            # Parse top level rules
            ll_rules = cls.__parse_rules(add_strict=strict and hl_spec['type'] == types.OBJECT,
                                         hl_rules=hl_spec['rules'])
            ll_spec = {
                rules.NULLABLE: rules.NULLABLE in [rule['name'] for rule in ll_rules],  # From Nullable rule to spec attribute
                'rules': [rule for rule in ll_rules if rule['name'] != rules.NULLABLE],  # Filter out 'nullable' rule
                'type': hl_spec['type']
            }
        except KeyError as e:
            raise SpecError('The key "{}" is required.'.format(e.args[0]))
        if 'elements' in hl_spec:
            # Validate that the 'elements' key is used only inside an 'array' type spec
            if hl_spec['type'] != types.ARRAY:
                raise SpecError('Only "{}" structures must define "elements"'.format(types.ARRAY))
            # Parse nested spec recursively
            ll_spec['elements'] = cls.parse(hl_spec['elements'], strict)
        if 'schema' in hl_spec:
            # Validate that the 'schema' key is used only inside an 'object' type spec
            if hl_spec['type'] != types.OBJECT:
                raise SpecError('Only "{}" structures must define a "schema"'.format(types.OBJECT))
            ll_spec['schema'] = {}
            required_keys = []
            for key, nested_spec in hl_spec['schema'].items():
                if rules.REQUIRED in nested_spec['rules']:
                    required_keys.append(key)
                # Parse nested spec recursively
                ll_spec['schema'][key] = cls.parse(hl_spec['schema'][key], strict)
            if required_keys:
                # Add 'required' rule to top level object
                ll_spec['rules'].append({'name': rules.REQUIRED, 'params': required_keys})
        return ll_spec

    @staticmethod
    def __parse_rule(hl_rule: str) -> dict:
        """ Parse a rule from string format to dict format """
        name_alias, *params = hl_rule.split(NAME_PARAM_SEP, maxsplit=1)
        match = ALIAS_RE.fullmatch(name_alias)
        if match is None:
            raise SpecError("""Rule "{}" is formatted incorrectly.\n
                                Rules must have the following format: {}""".format(hl_rule, RULE_FMT))
        name = match.group('name')
        alias = match.group('alias')
        ll_rule = {'name': name}
        if alias:
            ll_rule['alias'] = alias
        if params:
            # Split params string for every rule except for RegexRule
            if name != rules.REGEX:
                params = params[0].split(PARAMS_SEP)
            ll_rule['params'] = params
        return ll_rule

    @classmethod
    def __parse_rules(cls, add_strict: bool, hl_rules) -> list:
        """ Parse a high-level rule group """
        if isinstance(hl_rules, str):
            split_rules = hl_rules.split(RULE_SEP)
        else:
            split_rules = hl_rules
        if add_strict:
            split_rules.append(rules.STRICT)
        # Filter out 'required' rule
        # Parse every rule
        return [cls.__parse_rule(rule) for rule in split_rules if rules.REQUIRED not in rule]
