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
RULE_FMT = f'name[alias]{NAME_PARAM_SEP}param1{PARAMS_SEP}param2{PARAMS_SEP}param3'
RULE_SEP = '|'


class SpecParser:
    @classmethod
    def parse(cls, hl_spec: dict) -> dict:
        """ Parse a high-level spec into a low-level spec """
        try:
            # Parse top level rules
            ll_rules = cls.__parse_rules(hl_spec['rules'])
            ll_spec = {
                'nullable': 'nullable' in [rule['name'] for rule in ll_rules],  # From Nullable rule to spec attribute
                'rules': [rule for rule in ll_rules if rule['name'] != 'nullable'],  # Filter out 'nullable' rule
                'type': hl_spec['type']
            }
        except KeyError as e:
            raise SpecError(f'The key "{e.args[0]}" is required.')
        if 'elements' in hl_spec:
            # Validate that the 'elements' key is used only inside an 'array' type spec
            if hl_spec['type'] != types.ARRAY:
                raise SpecError(f'Only "{types.ARRAY}" structures must define "elements"')
            # Parse nested spec recursively
            ll_spec['elements'] = cls.parse(hl_spec['elements'])
        if 'schema' in hl_spec:
            # Validate that the 'schema' key is used only inside an 'object' type spec
            if hl_spec['type'] != types.OBJECT:
                raise SpecError(f'Only "{types.OBJECT}" structures must define a "schema"')
            ll_spec['schema'] = {}
            required_keys = []
            for key, nested_spec in hl_spec['schema'].items():
                if rules.REQUIRED in nested_spec['rules']:
                    required_keys.append(key)
                # Parse nested spec recursively
                ll_spec['schema'][key] = cls.parse(hl_spec['schema'][key])
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
            raise SpecError(f"""Rule "{hl_rule}" is formatted incorrectly.\n
                                Rules must have the following format: {RULE_FMT}""")
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
    def __parse_rules(cls, hl_rules) -> list:
        """ Parse a high-level rule group """
        if isinstance(hl_rules, str):
            split_rules = hl_rules.split(RULE_SEP)
        else:
            split_rules = hl_rules
        # Filter out 'required' rule
        # Parse every rule
        return [cls.__parse_rule(rule) for rule in split_rules if rules.REQUIRED not in rule]
