import re
from math import ceil

# Constants
BASE64_RE = re.compile(r'^data:(?P<type>[a-z]+)/(?P<format>[a-z]+);base64,(?P<data>.*)$')


def get_format(encoded_file: str) -> str:
    """ Retrieve the format of a base64 formatted file """
    match = BASE64_RE.match(encoded_file)
    if match is None:
        return ""
    return match.group('format')


def get_size(encoded_file: str) -> int:
    """ Calculate VERY ROUGHLY the size in bytes of a base64 formatted file """
    match = BASE64_RE.match(encoded_file)
    if match is None:
        return 0
    file = match.group('data')
    length = len(file) / 4 * 3
    if file.endswith('=='):
        length -= 2
    elif file.endswith('='):
        length -= 1
    return ceil(length)


def get_type(encoded_file: str) -> str:
    """ Retrieve the file-type of a base64 formatted file """
    match = BASE64_RE.match(encoded_file)
    if match is None:
        return ""
    return match.group('type')
