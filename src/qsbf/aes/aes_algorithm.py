"""
aes_algorithm.py

Research-grade AES implementation for QSBF.
"""

from src.qsbf.core.algorithm import Algorithm

from src.qsbf.aes.key_generator import AESKeyGenerator
from src.qsbf.aes.encryptor import AESEncryptor
from src.qsbf.aes.decryptor import AESDecryptor


class AESAlgorithm(Algorithm):

    def __init__(self, key_size=32):

        self.key_size = key_size

        self.key = None

        self.generator = AESKeyGenerator(key_size)

        self.encryptor = AESEncryptor()

        self.decryptor = AESDecryptor()

    @property
    def name(self):

        return "AES"

    def initialize(self):

        self.key = self.generator.generate()

    def generate_keys(self):

        self.key = self.generator.generate()

        return self.key

    def encrypt(self, plaintext: bytes):

        if self.key is None:

            self.generate_keys()

        return self.encryptor.encrypt(
            self.key,
            plaintext,
        )

    def decrypt(self, encrypted_data):

        if self.key is None:

            raise RuntimeError("AES key not initialized.")

        nonce, ciphertext = encrypted_data

        return self.decryptor.decrypt(
            self.key,
            nonce,
            ciphertext,
        )

    def benchmark(self):

        return {}