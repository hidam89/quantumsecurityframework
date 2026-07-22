"""
rsa_algorithm.py

Temporary RSA implementation for framework testing.
"""

from src.qsbf.core.algorithm import Algorithm


class RSAAlgorithm(Algorithm):
    """
    Temporary RSA algorithm implementation.
    """

    @property
    def name(self) -> str:
        return "RSA"

    def initialize(self) -> None:
        print("Initializing RSA")

    def generate_keys(self):
        """
        Temporary workload for benchmarking.
        """
        total = 0

        for i in range(500000):
            total += i

        return total

    def encrypt(self, plaintext: bytes) -> bytes:
        return plaintext

    def decrypt(self, ciphertext: bytes) -> bytes:
        return ciphertext

    def benchmark(self):
        return {}