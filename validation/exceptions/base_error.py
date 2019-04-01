""" Base Error """
from abc import abstractmethod

from .error import Error


class BaseError(Error):
    @staticmethod
    @abstractmethod
    def name() -> str:
        """ Specifies the name of the error """
