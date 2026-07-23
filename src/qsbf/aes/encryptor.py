"""
encryptor.py

AES-256-GCM Encryption Module
"""

import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class AESEncryptor:
    """
    AES-GCM Encryptor
    """

    def encrypt(self, key: bytes, plaintext: bytes):

        # GCM requires a unique nonce for every encryption
        nonce = os.urandom(12)

        aes = AESGCM(key)

        ciphertext = aes.encrypt(
            nonce,
            plaintext,
            None,
        )

        return nonce, ciphertext