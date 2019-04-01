""" Max Size """
from .rule import Rule
from ..constants import rules
from ..types import Base64EncodedFileType
from ..utils.base64file_utils import get_size


class MaxSizeRule(Rule):
    required_params = 1
    supported_types = (Base64EncodedFileType,)

    @staticmethod
    def name() -> str:
        return rules.MAX_SIZE

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the value's file size is greater than maxsize.
        return get_size(value) <= self.maxsize

    def _sanitize_params(self):
        # The file size is expressed in bytes.
        self.maxsize = int(self.params[0])
