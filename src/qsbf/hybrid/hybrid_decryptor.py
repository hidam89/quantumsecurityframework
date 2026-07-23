"""
hybrid_decryptor.py

Hybrid RSA-AES Decryption
"""

from src.qsbf.aes.decryptor import AESDecryptor
from src.qsbf.hybrid.package_parser import HybridPackageParser


class HybridDecryptor:

    def __init__(self, rsa_algorithm):

        self.rsa = rsa_algorithm

        self.package_parser = HybridPackageParser()

        self.aes_decryptor = AESDecryptor()

    def decrypt(self, package):

        (
            metadata,
            nonce,
            encrypted_key,
            ciphertext,
        ) = self.package_parser.parse(package)

        # Recover AES session key
        aes_key = self.rsa.decrypt(encrypted_key)

        # Recover plaintext
        plaintext = self.aes_decryptor.decrypt(
            aes_key,
            nonce,
            ciphertext,
        )

        return plaintext