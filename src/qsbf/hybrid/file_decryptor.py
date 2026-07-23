"""
file_decryptor.py

Decrypt files using the Hybrid RSA-AES module.
"""

from src.qsbf.fileio.file_reader import FileReader
from src.qsbf.fileio.file_writer import FileWriter
from src.qsbf.hybrid.hybrid_decryptor import HybridDecryptor


class HybridFileDecryptor:
    """
    Reads an encrypted .qsbf file, decrypts it,
    and writes the recovered plaintext.
    """

    def __init__(self, rsa_algorithm):

        self.reader = FileReader()

        self.writer = FileWriter()

        self.decryptor = HybridDecryptor(rsa_algorithm)

    def decrypt_file(
        self,
        input_file,
        output_file,
    ):

        package = self.reader.read(input_file)

        plaintext = self.decryptor.decrypt(package)

        self.writer.write(
            output_file,
            plaintext,
        )

        return output_file