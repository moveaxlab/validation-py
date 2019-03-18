""" Error """
from abc import ABC, abstractmethod


class Error(ABC, Exception):
    @abstractmethod
    def to_json(self) -> dict:
        """ Output errors as JSON string """
