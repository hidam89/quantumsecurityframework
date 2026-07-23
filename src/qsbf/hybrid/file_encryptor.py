"""
file_encryptor.py

Encrypt files using the Hybrid RSA-AES module.
"""

from pathlib import Path

from src.qsbf.fileio.file_reader import FileReader
from src.qsbf.fileio.file_writer import FileWriter
from src.qsbf.hybrid.hybrid_encryptor import HybridEncryptor


class HybridFileEncryptor:

    def __init__(self, rsa_algorithm):

        self.reader = FileReader()

        self.writer = FileWriter()

        self.encryptor = HybridEncryptor(rsa_algorithm)

    def encrypt_file(
        self,
        input_file,
        output_file,
    ):

        plaintext = self.reader.read(input_file)

        package = self.encryptor.encrypt(plaintext)

        self.writer.write(
            output_file,
            package,
        )

        return package