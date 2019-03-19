""" File Type """
from .rule import Rule
from ..constants import rules
from ..types import Base64EncodedFileType
from ..utils.base64file_utils import get_type


class FileTypeRule(Rule):
    required_params = 1
    supported_types = (Base64EncodedFileType,)

    @staticmethod
    def name() -> str:
        return rules.FILE_TYPE

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the type of the given file is not equal to the given type.
        return get_type(value) == self.type

    def _sanitize_params(self):
        self.type = self.params[0]
