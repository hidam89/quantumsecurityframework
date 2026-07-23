"""
key_generator.py

AES Key Generator
"""

import os


class AESKeyGenerator:
    """
    Generates AES symmetric keys.
    """

    def __init__(self, key_size=32):
        """
        key_size:
            16 = AES-128
            24 = AES-192
            32 = AES-256
        """
        self.key_size = key_size

    def generate(self):

        return os.urandom(self.key_size)