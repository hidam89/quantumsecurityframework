"""
hybrid_encryptor.py

Hybrid RSA-AES Encryption
"""

from src.qsbf.aes.key_generator import AESKeyGenerator
from src.qsbf.aes.encryptor import AESEncryptor

from src.qsbf.hybrid.metadata import HybridMetadata
from src.qsbf.hybrid.package_builder import HybridPackageBuilder


class HybridEncryptor:

    def __init__(self, rsa_algorithm):

        self.rsa = rsa_algorithm

        self.aes_key_generator = AESKeyGenerator()

        self.aes_encryptor = AESEncryptor()

        self.package_builder = HybridPackageBuilder()

    def encrypt(self, plaintext: bytes):

        # Generate AES-256 key
        aes_key = self.aes_key_generator.generate()

        # Encrypt plaintext
        nonce, ciphertext = self.aes_encryptor.encrypt(
            aes_key,
            plaintext,
        )

        # Encrypt AES key using RSA
        encrypted_key = self.rsa.encrypt(aes_key)

        metadata = HybridMetadata(

            version="1.0",

            algorithm="Hybrid RSA-AES",

            rsa_key_size=self.rsa.key_size,

            aes_key_size=len(aes_key) * 8,

            nonce_length=len(nonce),

            encrypted_key_length=len(encrypted_key),

            ciphertext_length=len(ciphertext),
        )

        package = self.package_builder.build(
            metadata=metadata,
            nonce=nonce,
            encrypted_key=encrypted_key,
            ciphertext=ciphertext,
        )

        return package