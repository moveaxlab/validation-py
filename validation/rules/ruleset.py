from .rule import Rule


class RuleSet(object):

    @classmethod
    def from_description(cls, description, spec):

        if isinstance(description, str):
            rules = description.split('|')
        else:
            rules = description

        return cls([Rule.create(rule, spec) for rule in rules])

    def __init__(self, rules):
        self.rules = rules

    def __iter__(self):
        return iter(self.rules)
