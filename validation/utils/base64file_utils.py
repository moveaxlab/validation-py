# FIXME: get_format and get_type are the same function!!
import re

# Constants
BASE64_RE = re.compile(r'^data:[a-z]+/([a-z]+);base64,.*$')


def get_format(encoded_file):
    match = BASE64_RE.match(encoded_file)
    if match is None:
        return ""
    return match.groups()[0]


def get_size(encoded_file):
    match = BASE64_RE.match(encoded_file)
    if match is None:
        return 0
    file = match.groups()[0]
    length = len(file) / 4 * 3
    if file.endswith('=='):
        length -= 2
    elif file.endswith('='):
        length -= 1
    return length


def get_type(encoded_file):
    match = BASE64_RE.match(encoded_file)
    if match is None:
        return ""
    return match.groups()[0]
