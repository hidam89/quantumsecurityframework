"""
rsa_algorithm.py

Research-grade RSA implementation for QSBF.
"""

from src.qsbf.core.algorithm import Algorithm
from src.qsbf.rsa.key_generator import RSAKeyGenerator
from src.qsbf.rsa.encryptor import RSAEncryptor
from src.qsbf.rsa.decryptor import RSADecryptor


class RSAAlgorithm(Algorithm):

    def __init__(self, key_size: int = 2048):

        self.key_size = key_size

        self.private_key = None
        self.public_key = None

        self.generator = RSAKeyGenerator(key_size)

        self.encryptor = RSAEncryptor()

        self.decryptor = RSADecryptor()

    @property
    def name(self):

        return "RSA"

    def initialize(self):

        self.private_key, self.public_key = self.generator.generate()

    def generate_keys(self):

        self.private_key, self.public_key = self.generator.generate()

        return self.private_key, self.public_key

    def encrypt(self, plaintext: bytes):

        if self.public_key is None:
            self.generate_keys()

        return self.encryptor.encrypt(
            self.public_key,
            plaintext
        )

    def decrypt(self, ciphertext: bytes):

        if self.private_key is None:
            self.generate_keys()

        return self.decryptor.decrypt(
            self.private_key,
            ciphertext
        )

    def benchmark(self):

        return {}