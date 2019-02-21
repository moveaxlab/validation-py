import re

def get_type(encoded_file):
    regex = re.compile(r'^data:([a-z]+)/[a-z]+;base64,.*$')
    match = regex.match(encoded_file)
    if match is None:
        return ""
    return match.groups()[0]


def get_format(encoded_file):
    regex = re.compile(r'^data:[a-z]+/([a-z]+);base64,.*$')
    match = regex.match(encoded_file)
    if match is None:
        return ""
    return match.groups()[0]

def get_size(encoded_file):
    regex = re.compile(r'^data:[a-z]+/[a-z]+;base64,(.*)$')
    match = regex.match(encoded_file)
    if match is None:
        return 0
    file = match.groups()[0]
    length = len(file) / 4 * 3
    if file.endswith('=='):
        length -= 2
    elif file.endswith('='):
        length -= 1
    return length

