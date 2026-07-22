"""
algorithm.py

Abstract base interface for all cryptographic algorithms.
"""

from abc import ABC, abstractmethod
from typing import Any


class Algorithm(ABC):
    """
    Base interface for every cryptographic algorithm.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns algorithm name.
        """
        raise NotImplementedError

    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize algorithm.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_keys(self) -> Any:
        """
        Generate cryptographic keys.
        """
        raise NotImplementedError

    @abstractmethod
    def encrypt(self, plaintext: bytes) -> bytes:
        """
        Encrypt plaintext.
        """
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, ciphertext: bytes) -> bytes:
        """
        Decrypt ciphertext.
        """
        raise NotImplementedError

    @abstractmethod
    def benchmark(self) -> dict:
        """
        Execute benchmark.
        """
        raise NotImplementedError