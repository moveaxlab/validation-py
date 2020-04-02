""" Phone Type """
import phonenumbers

from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import PhoneType


class PhoneTypeRule(Rule):
    supported_types = (PhoneType,)

    @staticmethod
    def name() -> str:
        return rules.PHONE_TYPE

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the format of the given file is not in the formats list.
        try:
            number = phonenumbers.parse(value, None)
        except phonenumbers.NumberParseException:
            return False

        phoneType = phonenumbers.number_type(number)

        if phoneType == phonenumbers.PhoneNumberType.MOBILE:
            return self.phoneType == 'mobile'
        elif phoneType == phonenumbers.PhoneNumberType.FIXED_LINE:
            return self.phoneType == 'landline'
        elif phoneType == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            return True
        else:
            return False

    def _sanitize_params(self):
        if not self.params or len(self.params) != 1:
            raise SpecError('Provide a phone type parameter')
        self.phoneType = self.params[0]
        if self.phoneType != 'mobile' and self.phoneType != 'landline':
            raise SpecError('Invalid phone type specified')
