"""
encryptor.py

RSA Encryption Module
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class RSAEncryptor:
    """
    RSA encryption using OAEP padding.
    """

    def encrypt(self, public_key, plaintext: bytes) -> bytes:
        """
        Encrypt plaintext using RSA-OAEP.

        Args:
            public_key: RSA public key.
            plaintext: Plaintext bytes.

        Returns:
            Encrypted ciphertext.
        """

        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()
                ),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return ciphertext