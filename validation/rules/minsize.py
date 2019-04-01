""" Min Size """
from .rule import Rule
from ..constants import rules
from ..types import Base64EncodedFileType
from ..utils.base64file_utils import get_size


class MinSizeRule(Rule):
    required_params = 1
    supported_types = (Base64EncodedFileType,)

    @staticmethod
    def name() -> str:
        return rules.MIN_SIZE

    def _abides_by_the_rule(self, value):
        return get_size(value) >= self.minsize

    def _sanitize_params(self):
        # The file size is expressed in bytes.
        self.minsize = int(self.params[0])
