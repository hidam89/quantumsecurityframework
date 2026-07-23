"""
key_generator.py

RSA Key Generator for the Quantum Security Benchmarking Framework (QSBF).
"""

from cryptography.hazmat.primitives.asymmetric import rsa


class RSAKeyGenerator:
    """
    Generates RSA public/private key pairs.
    """

    def __init__(self, key_size: int = 2048):
        """
        Initialize the key generator.

        Args:
            key_size: RSA key size in bits.
        """
        self.key_size = key_size

    def generate(self):
        """
        Generate RSA private and public keys.

        Returns:
            tuple:
                (private_key, public_key)
        """

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
        )

        public_key = private_key.public_key()

        return private_key, public_key