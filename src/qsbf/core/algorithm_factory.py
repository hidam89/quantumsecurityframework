"""
algorithm_factory.py

Factory responsible for creating algorithm instances.
"""

from typing import Type

from src.qsbf.core.algorithm import Algorithm


class AlgorithmFactory:
    """
    Factory for creating cryptographic algorithm instances.
    """

    _algorithms: dict[str, Type[Algorithm]] = {}

    @classmethod
    def register(cls, name: str, algorithm_class: Type[Algorithm]) -> None:
        """
        Register a new algorithm.
        """
        cls._algorithms[name.upper()] = algorithm_class

    @classmethod
    def create(cls, name: str) -> Algorithm:
        """
        Create an algorithm instance.
        """
        algorithm = cls._algorithms.get(name.upper())

        if algorithm is None:
            raise ValueError(f"Unsupported algorithm: {name}")

        return algorithm()