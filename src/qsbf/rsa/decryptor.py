"""
decryptor.py

RSA Decryption Module
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class RSADecryptor:
    """
    RSA decryption using OAEP padding.
    """

    def decrypt(self, private_key, ciphertext: bytes) -> bytes:
        """
        Decrypt RSA ciphertext.

        Args:
            private_key: RSA private key.
            ciphertext: Encrypted bytes.

        Returns:
            Original plaintext bytes.
        """

        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()
                ),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return plaintext