""" File Format """
from .rule import Rule
from ..constants import rules
from ..exceptions import SpecError
from ..types import Base64EncodedFileType
from ..utils.base64file_utils import get_format


class FileFormatRule(Rule):
    supported_types = (Base64EncodedFileType,)

    @staticmethod
    def name() -> str:
        return rules.FILE_FORMAT

    def _abides_by_the_rule(self, value) -> bool:
        # Fail when the format of the given file is not in the formats list.
        return get_format(value) in self.formats

    def _sanitize_params(self):
        if not self.params:
            raise SpecError('At least one file format is required')
        self.formats = self.params
