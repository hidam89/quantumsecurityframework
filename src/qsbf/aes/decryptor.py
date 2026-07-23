"""
decryptor.py

AES-256-GCM Decryption Module
"""

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class AESDecryptor:
    """
    AES-GCM Decryptor
    """

    def decrypt(
        self,
        key: bytes,
        nonce: bytes,
        ciphertext: bytes,
    ):

        aes = AESGCM(key)

        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None,
        )

        return plaintext