"""
key_manager.py

RSA Key Storage and Loading Module
"""

from pathlib import Path

from cryptography.hazmat.primitives import serialization


class RSAKeyManager:
    """
    Save and load RSA keys in PEM format.
    """

    def __init__(self, key_directory="data/keys"):
        self.key_directory = Path(key_directory)
        self.key_directory.mkdir(parents=True, exist_ok=True)

    def save_keys(self, private_key, public_key, key_size: int):
        """
        Save RSA private and public keys.
        """

        private_path = self.key_directory / f"rsa_{key_size}_private.pem"
        public_path = self.key_directory / f"rsa_{key_size}_public.pem"

        with open(private_path, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )

        with open(public_path, "wb") as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

        return private_path, public_path

    def load_private_key(self, key_size: int):
        """
        Load RSA private key.
        """

        private_path = self.key_directory / f"rsa_{key_size}_private.pem"

        with open(private_path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )

        return private_key

    def load_public_key(self, key_size: int):
        """
        Load RSA public key.
        """

        public_path = self.key_directory / f"rsa_{key_size}_public.pem"

        with open(public_path, "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read()
            )

        return public_key