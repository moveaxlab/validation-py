# Validation library
[![Build Status](https://travis-ci.com/moveaxlab/validation-py.svg?branch=master)](https://travis-ci.com/moveaxlab/validation-py)
[![Coverage Status](https://coveralls.io/repos/github/moveaxlab/validation-py/badge.svg?branch=master)](https://coveralls.io/github/moveaxlab/validation-py?branch=master)
![GitHub](https://img.shields.io/github/license/moveaxlab/validation-py.svg)
![PyPI](https://img.shields.io/pypi/v/moveax-validation.svg?style=popout)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/moveax-validation.svg)

## Installation
- Install from [Pypi](https://pypi.org/project/moveax-validation/):

    ```console
    $ pip install moveax-validation
            --- or ---
    $ poetry add moveax-validation
    ```

## Usage
- Simple example:

    ```python
    >>> from validation import ValidatorFactory

    >>> data = ['foo', 'bar']
    >>> schema = {
        'elements': {
            'rules': ['minlen:3']
            'type': 'string'
        },
        'rules': ['maxlen:3'],
        'type': 'array'
    }
    >>> validator = ValidatorFactory.make(schema)
    >>> validator.validate(data)
    ```

## Testing
- Run the test suite with:

    ```console
    $ poetry run coverage run unit.py
    ```
